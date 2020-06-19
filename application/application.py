"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""

import os
from application.container import IocContainer
from services.AuthSetServiceException import AuthSetServiceException
from services.StartAppServiceException import StartAppServiceException
from services.StopAppServiceException import StopAppServiceException
from application.applicationException import ApplicationException

startUpMessage = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'startUpMessage'), 'r').read()


class DevOpsPipelineApp:
    """

    """
    def __init__(self):
        self.stopApp = IocContainer.stopAppService()
        self.autoSet = IocContainer.autoSetService()
        self.mailSet = IocContainer.mailSetService()
        self.startApp = IocContainer.startAppService()
        self.log = IocContainer.appLog().log

    def run(self):
        try:
            self.log.info(startUpMessage)

            self.autoSet.run()
            self.mailSet.run()
            self.stopApp.run()
            self.startApp.run()

        except (AuthSetServiceException, StartAppServiceException, StopAppServiceException) as ex:
            raise ApplicationException("(DevOpsPipelineApp.run method)->{0}".format(ex))
