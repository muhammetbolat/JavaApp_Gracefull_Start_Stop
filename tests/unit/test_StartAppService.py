import pytest
import random
from tests.testContainer import IocContainer
from services.StopAppService import StopAppService
from services.StopAppServiceException import StopAppServiceException
import time
import os
from pytest import raises


@pytest.fixture()
def startAppService():
    """

    :return:
    """
    startAppService = IocContainer.startAppService()

    return startAppService

@pytest.fixture()
def stopAppService():
    """

    :return:
    """
    stopAppService = IocContainer.stopAppService()

    return stopAppService


def test_startApp(startAppService, stopAppService):
    startAppService.startApp(startAppService.genericAppConfig.appTargetFile,
                             startAppService.genericAppConfig.startUpCommand,
                             basedir=os.path.dirname(os.path.abspath(__file__)))
    time.sleep(30)
    stopAppService.killRunningAppProcess(stopAppService.genericAppConfig.appTargetFile)
    os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nohup.out'))
    assert True
