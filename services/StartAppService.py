"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""
import os
import time
from config.SqlConfig import SqlConfig
from config.GenericConfig import GenericConfig
from infrastructor.LogUtil import Logger
from libs.DbUtil import Oracle
from services.StartAppServiceException import StartAppServiceException
from libs.ProcessUtil import ProcessUtil


class StartAppService:
    """
    Start Application Service Class
    """
    def __init__(self,
                 appLog: Logger = None,
                 db: Oracle = None,
                 sqlConfig: SqlConfig = None,
                 genericAppConfig: GenericConfig = None
                 ) -> None:
        self.db = db
        self.log = appLog.log
        self.sqlConfig = sqlConfig
        self.genericAppConfig = genericAppConfig

    def startApp(self, appTargetFile, startUpCommand, basedir=os.path.dirname(os.path.abspath(__file__))):
        """
        This method starts application.
        :param appTargetFile: location of the jar file.
        :param startUpCommand: startUp comment
        :param basedir: base direction of the project.
        :return: void.
        """
        try:
            self.log.info("Basedir is setting to '{0}'".format(basedir))
            os.chdir(basedir)

            self.log.info("Java path is setting to {0}".format(self.genericAppConfig.javaPath))
            os.environ["PATH"] = self.genericAppConfig.javaPath

            self.log.info("application is starting up. The command is '{0}'".format(startUpCommand))
            os.system(startUpCommand)

            self.log.info("Basedir is back to setting to {0}".format(os.path.dirname(os.path.abspath(__file__))))
            os.chdir(os.path.dirname(os.path.abspath(__file__)))

            self.log.info("Application is waiting to run in 30 seconds...")
            time.sleep(30)

            self.log.info("Checking the process ...")
            workingProcess = ProcessUtil.findProcByCommandLineArgs(appTargetFile)

            if not len(workingProcess):
                self.log.error("Application hasn't started yet. Please check it. !!!")
            elif len(workingProcess) == 1:
                self.log.info("{0} target file has started -> {1}".
                              format(appTargetFile, workingProcess))
            else:
                self.log.error("One more application is running -> {0}".format(workingProcess))

        except Exception as ex:
            raise StartAppServiceException("(startApp method)->{0}".format(ex))

    def run(self):
        """
        The entry point of the service.
        :return: void
        """
        self.startApp(self.genericAppConfig.appTargetFile,
                      self.genericAppConfig.startUpCommand,
                      self.genericAppConfig.baseDir)
