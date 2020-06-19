import pytest
import random
from tests.testContainer import IocContainer
from libs.ProcessUtil import ProcessUtil
import time

@pytest.fixture()
def stopAppService():
    """

    :return:
    """
    stopAppService = IocContainer.stopAppService()
    return stopAppService


def test_isApplicationReadyToStop(stopAppService):
    """

    :param stopAppService:
    :return:
    """
    route_ID = "TEST_ROUTE_{}".format(random.randint(0, 1000))

    stopAppService.db.insert(stopAppService.sqlConfig.stopAllRoutesInsert.format(route_ID))

    appStatus = stopAppService.isApplicationReadyToStop(stopAppService.sqlConfig.routesSelectQuery, route_ID)

    stopAppService.db.delete(stopAppService.sqlConfig.stopAllRoutesDelete.format(route_ID))

    assert not appStatus


def test_waitUntilCriticalRoutesToStop(stopAppService):
    """

    :param stopAppService:
    :return:
    """
    stopAppService.db.update(stopAppService.sqlConfig.updateRoutesStopInformation)

    stopAppService.waitUntilCriticalRoutesToStop(stopAppService.sqlConfig.criticalRoutesStopCheck,
                                                 stopAppService.stopAppConfig.routeTableCheckInterval,
                                                 stopAppService.sqlConfig.updateRoutesStopInformation
                                                 )
    assert True



