import os
from dependency_injector import providers, containers
from libs.DbUtil import Oracle
from infrastructor.LogUtil import Logger
from services.AuthSetService import AutoSetService
from services.StopAppService import StopAppService
from services.StartAppService import StartAppService
from application.configuration import Configurations


class IocContainer(containers.DeclarativeContainer):
    configuration = Configurations(confFile='test.devops.properties.yml',
                                   confPath=os.path.dirname(os.path.abspath(__file__)))

    appDb = providers.Singleton(Oracle,
                                dbConf=configuration.getDataBaseConfig())

    appLog = providers.Factory(Logger,
                               logConfig=configuration.getAppLogConfig())

    autoSetService = providers.Factory(AutoSetService,
                                       appLog,
                                       configuration.getAuthSetConfig())

    stopAppService = providers.Factory(StopAppService,
                                       appLog,
                                       appDb,
                                       configuration.getStopAppConfig(),
                                       configuration.getSqlConfig(),
                                       configuration.getGenericConfig()
                                       )

    startAppService = providers.Factory(StartAppService,
                                        appLog,
                                        configuration.getStopAppConfig(),
                                        configuration.getSqlConfig(),
                                        configuration.getGenericConfig()
                                        )
