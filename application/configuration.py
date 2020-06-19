"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""

import os

from config.StopAppConfig import StopAppConfig
from libs.FileUtil import FileUtil
from config.SqlConfig import SqlConfig
from config.GenericConfig import GenericConfig
from config.DataBaseConfig import DataBaseConfig
from config.LoggerConfig import LoggerConfig
from config.AuthConfig import AuthConfig


class Configurations:
    """
    This class coordinate all config classes.
    """

    def __init__(self, confFile, confPath=os.path.dirname(os.path.abspath(__file__))):
        ################################################################################################################
        cfg = FileUtil.readYaml(os.path.join(confPath, confFile))

        ################################################################################################################
        # SQL Configuration
        routesSelectQuery = os.getenv('routes.select.query', cfg['routes.select.query'])
        stopAllRoutesInsert = os.getenv('stop.all.routes.insert', cfg['stop.all.routes.insert'])
        stopAllRoutesDelete = os.getenv('stop.all.routes.delete', cfg['stop.all.routes.delete'])
        criticalRoutesStopCheck = os.getenv('critical.routes.stop.check', cfg['critical.routes.stop.check'])
        updateRoutesStopInformation = os.getenv('update.routes.stop.information', cfg['update.routes.stop.information'])

        self.__sqlConfig = SqlConfig(routesSelectQuery,
                                     stopAllRoutesInsert,
                                     stopAllRoutesDelete,
                                     criticalRoutesStopCheck,
                                     updateRoutesStopInformation)

        ################################################################################################################
        # Generic Configuration
        appTargetFile = os.getenv('APP.TARGET.FILE', cfg['APP.TARGET.FILE'])
        appRunScript = os.getenv('APP.RUN.SCRIPT', cfg['APP.RUN.SCRIPT'])
        baseDir = os.getenv('base.dir', cfg['base.dir'])
        startUpCommand = os.getenv('startup.command', cfg['startup.command'])
        javaPath = os.getenv('java.path', cfg['java.path'])

        self.__genericConfig = GenericConfig(appTargetFile, appRunScript, baseDir, startUpCommand, javaPath)

        ################################################################################################################
        # DataBase Configuration

        dbHost = os.getenv('DB.HOST', cfg['DB']['HOST'])
        dbPort = os.getenv('DB.PORT', cfg['DB']['PORT'])
        dbName = os.getenv('DB.NAME', cfg['DB']['NAME'])
        dbUserName = os.getenv('DB.USERNAME', cfg['DB']['USERNAME'])
        dbPassword = os.getenv('DB.PASSWORD', cfg['DB']['PASSWORD'])

        self.__dataBaseConfig = DataBaseConfig(dbHost, dbPort, dbName, dbUserName, dbPassword)

        ################################################################################################################
        # Logger Configurations
        logHeader = os.getenv('LOG.HEADER', cfg['LOG']['HEADER'])
        logPath = os.getenv('LOG.BASE.PATH', cfg['LOG']['BASE.PATH'])
        devOpsApp = os.getenv('LOG.DEVOPS.APP', cfg['LOG']['DEVOPS.APP'])

        self.__appLogConfig = LoggerConfig(logHeader, logPath, devOpsApp)

        ################################################################################################################
        # Authorization Configuration
        authSetTargetFile = os.getenv('TARGET.FILE', cfg['TARGET.FILE'])
        authValues = os.getenv('AUTHSET', cfg['AUTHSET'])

        self.__authSetConfig = AuthConfig(authSetTargetFile, authValues)

        ################################################################################################################
        # Authorization Configuration
        mailSetTargetFile = os.getenv('MAIL_PROPERTIES.TARGET.FILE', cfg['MAIL_PROPERTIES.TARGET.FILE'])
        mailValues = os.getenv('MAILSET', cfg['MAILSET'])

        self.__mailSetConfig = AuthConfig(mailSetTargetFile, mailValues)

        ################################################################################################################
        # Stop application Configuration
        stopAllRouteID = os.getenv('STOP.ALL.ROUTE.ID', cfg['STOP.ALL.ROUTE.ID'])
        routeTableCheckInterval = os.getenv('ROUTE.TABLE.CHECK.INTERVAL', cfg['ROUTE.TABLE.CHECK.INTERVAL'])

        self.__stopAppConfig = StopAppConfig(stopAllRouteID, routeTableCheckInterval)

    def getSqlConfig(self): return self.__sqlConfig

    def getGenericConfig(self): return self.__genericConfig

    def getDataBaseConfig(self): return self.__dataBaseConfig

    def getAppLogConfig(self): return self.__appLogConfig

    def getAuthSetConfig(self): return self.__authSetConfig

    def getMailSetConfig(self): return self.__mailSetConfig

    def getStopAppConfig(self): return self.__stopAppConfig
