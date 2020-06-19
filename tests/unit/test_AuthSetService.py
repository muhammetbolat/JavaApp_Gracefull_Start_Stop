import pytest
import os
from tests.testContainer import IocContainer


@pytest.fixture()
def autoSetService():
    autoSetService = IocContainer.autoSetService()
    return autoSetService


def test_getTargetFile(autoSetService):
    """
    The test scenario try to get a file.
    :param autoSetService: autoSetService object
    :return: If the pass the test, It returns True, otherwise False
    """
    targetFileData = autoSetService.getTargetFile(autoSetService.config.targetFile)
    assert len(targetFileData) > 0


def test_replacingOperation(autoSetService):
    """
    The test scenario try to replace the given parameter to target file.
    :param autoSetService: autoSetService object
    :return: If the pass the test, It returns True, otherwise False
    """
    authSet = {'main.jdbc.url': 'jdbc:oracle:thin:@//acrab.turkcell.tgc:1521/ESSPRO',
               'main.jdbc.username': 'root',
               'main.jdbc.password': 'root_passwd'
               }

    targetFileData = "main.jdbc.url=jdbc:oracle:thin:@//acrab.turkcell.tgc:1521/UC4TEST\n" \
                     "main.jdbc.username=ESS_REV_PRP\n" \
                     "main.jdbc.password=t_ESS_REV_DEV\n" \
                     "main.jdbc.test=test"

    targetFileDataFinal = autoSetService.replacingOperation(authSet, targetFileData)

    for key, value in authSet.items():
        if not (value in targetFileDataFinal):
            assert False

        assert True


def test_putTargetFile(autoSetService):
    """
    The test scenario try to write a file. It produces dummy data.
    :param autoSetService: autoSetService object
    :return: If the pass the test, It returns True, otherwise False
    """
    testTargetFile = "testProperties.txt"
    testTargetData = "dummyData"
    autoSetService.putTargetFile(testTargetFile, testTargetData)

    with open(testTargetFile) as f:
        finalData = f.read()

    result = True
    if not testTargetData == finalData:
        result = False

    os.remove(testTargetFile)

    assert result
