"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""
import time
from config.StopAppConfig import StopAppConfig
from config.SqlConfig import SqlConfig
from config.GenericConfig import GenericConfig
from infrastructor.LogUtil import Logger
from libs.DbUtil import Oracle
from libs.ProcessUtil import ProcessUtil
from services.StopAppServiceException import StopAppServiceException


class StopAppService:
    """
    Stop Application Service Class
    """
    def __init__(self,
                 appLog: Logger = None,
                 db: Oracle = None,
                 stopAppConfig: StopAppConfig = None,
                 sqlConfig: SqlConfig = None,
                 genericAppConfig: GenericConfig = None
                 ) -> None:
        self.db = db
        self.log = appLog.log
        self.stopAppConfig = stopAppConfig
        self.sqlConfig = sqlConfig
        self.genericAppConfig = genericAppConfig

    def isApplicationReadyToStop(self, routesSelectQuery, stopRouteId) -> bool:
        """
        The predicated method checks the application where ready to stop or not.
        :param routesSelectQuery: sql query which is checked the stopped route id is available.
        :param stopRouteId: the route name which is stopped all system.
        """
        try:
            stopRoutesTableRecords = self.db.query(routesSelectQuery.format(stopRouteId))

            for routeId, stopDesc, stoppedTime, stoppedUser in stopRoutesTableRecords:
                if routeId == stopRouteId:
                    self.log.error("application has already stopped -> USER:{0}, STOP TIME:{1}, STOP DESCRIPTION:{2}".
                                   format(stoppedUser, stoppedTime, stopDesc))
                    return False

            return True

        except Exception as ex:
            raise StopAppServiceException("(isApplicationReadyToStop method)->{0}".format(ex))

    def waitUntilCriticalRoutesToStop(self, criticalRoutesStopCheck,
                                      routeTableCheckInterval,
                                      updateRoutesStopInformation):
        """
        The method checks the working routes on DB and waits the critical ones to finish.
        End of the method, non-critical working routes will be labeled as finished by Jenkins pipeline.
        :param criticalRoutesStopCheck: SQL script to check critical ones.
        :param routeTableCheckInterval: Total the max time to wait.
        :param updateRoutesStopInformation: update the non-critical routes.
        :return:
        """
        try:
            loopLimit = routeTableCheckInterval // 10

            i = 0
            while True:
                logOutput = '---> {}% Application will be stopped.'.format(int((i / loopLimit) * 100))
                print(logOutput)
                self.log.info(logOutput)

                time.sleep(10)
                workingRoutes = self.db.query(criticalRoutesStopCheck)
                if not workingRoutes:
                    self.log.info("All critical routes are done. :)")
                    break

                for route in workingRoutes:
                    print("{} is still running... :(".format(route[0]))
                    self.log.info("{} is still running... :(".format(route[0]))

                if loopLimit == i:
                    self.log.info("Critical Routes haven't finish in the given time. App is gonna force to kill.")
                    break
                i += 1

            self.log.info("Routes which has finish time as NULL is updated in DB.")
            self.db.update(updateRoutesStopInformation)

        except Exception as ex:
            raise StopAppServiceException("(waitUntilCriticalRoutesToStop method)->{0}".format(ex))

    def killRunningAppProcess(self, appTargetFile):
        """

        :param appTargetFile:
        :return:
        """
        try:
            workingProcess = ProcessUtil.findProcByCommandLineArgs(appTargetFile)

            if not workingProcess:
                self.log.info('There is no process to kill {0}. Pipeline is going on...'.format(appTargetFile))
                return

            # Kill running App Process
            for proc in workingProcess:
                self.log.info('PID:{} is ready to kill...'.format(proc.pid))
                ProcessUtil.killProcess(proc)
                self.log.info('PID:{} is killed...'.format(proc.pid))

            # Check Process Again
            workingProcess = ProcessUtil.findProcByCommandLineArgs(appTargetFile)
            for proc in workingProcess:
                self.log.error('PID:{} is still alive...'.format(proc.pid))
                raise StopAppServiceException("*** !!! PID:{} is still alive *** !!!".format(proc.id))

        except Exception as ex:
            raise StopAppServiceException("(killRunningAppProcess method)->{0}".format(ex))

    def run(self):
        """
        The entry point of the service.
        :return void
        """
        try:
            self.log.info("Control the application's status to stop...")
            appStatus = self.isApplicationReadyToStop(self.sqlConfig.routesSelectQuery,
                                                      self.stopAppConfig.stopAllRouteID)
            if appStatus:
                self.log.info(
                    "application stop route({0}) is inserted to table...".format(self.stopAppConfig.stopAllRouteID))
                self.db.insert(self.sqlConfig.stopAllRoutesInsert.format(self.stopAppConfig.stopAllRouteID))

            self.waitUntilCriticalRoutesToStop(self.sqlConfig.criticalRoutesStopCheck,
                                               self.stopAppConfig.routeTableCheckInterval,
                                               self.sqlConfig.updateRoutesStopInformation)

            self.killRunningAppProcess(self.genericAppConfig.appTargetFile)

            self.db.delete(self.sqlConfig.stopAllRoutesDelete.format(self.stopAppConfig.stopAllRouteID))
            self.log.info("Stop all route's record is deleted in database...")

        except Exception as ex:
            raise StopAppServiceException("(run method)->{0}".format(ex))
