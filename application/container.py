"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""

import os
from pathlib import Path
from dependency_injector import providers, containers
from application.configuration import Configurations
from libs.DbUtil import Oracle
from infrastructor.LogUtil import Logger
from services.AuthSetService import AutoSetService
from services.StopAppService import StopAppService
from services.StartAppService import StartAppService


class IocContainer(containers.DeclarativeContainer):

    configuration = Configurations(confFile='devops.properties.yml',
                                   confPath='/data01'
                                   )

    appDb = providers.Singleton(Oracle,
                                dbConf=configuration.getDataBaseConfig())

    appLog = providers.Singleton(Logger,
                                 logConfig=configuration.getAppLogConfig())

    autoSetService = providers.Singleton(AutoSetService,
                                         appLog,
                                         configuration.getAuthSetConfig())

    mailSetService = providers.Singleton(AutoSetService,
                                         appLog,
                                         configuration.getMailSetConfig())

    stopAppService = providers.Singleton(StopAppService,
                                         appLog,
                                         appDb,
                                         configuration.getStopAppConfig(),
                                         configuration.getSqlConfig(),
                                         configuration.getGenericConfig()
                                         )

    startAppService = providers.Singleton(StartAppService,
                                          appLog,
                                          configuration.getStopAppConfig(),
                                          configuration.getSqlConfig(),
                                          configuration.getGenericConfig()
                                          )
