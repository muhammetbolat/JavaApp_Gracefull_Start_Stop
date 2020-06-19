"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""
import re
from config.AuthConfig import AuthConfig
from libs.FileUtil import FileUtil
from infrastructor.LogUtil import Logger
from services.AuthSetServiceException import AuthSetServiceException


class AutoSetService:
    """
    Authorization Service Class
    """
    def __init__(self,
                 appLog: Logger = None,
                 config: AuthConfig = None) -> None:
        """
        AutoSetService class is the core of the changing critical information to target file.
        :param appLog: log object
        :param config: AutoSetService specified AuthConfig type configuration object.
        """
        self.config = config
        self.log = appLog.log

    @staticmethod
    def getTargetFile(targetFileName) -> str:
        """
        get the target file's data as str.
        :param targetFileName: name of the target file.
        :return: data as string.
        """
        try:
            targetFileData = FileUtil.readFile(filename=targetFileName)
        except Exception as ex:
            raise AuthSetServiceException("(getTargetFile method)->{0}".format(ex))

        return targetFileData

    @staticmethod
    def putTargetFile(filename, data):
        """
        put the wanted information which is defined by operation guy to target file.
        :param filename: name of the target file.
        :param data: data as string
        :return:
        """
        try:
            FileUtil.writeFile(filename=filename, data=data)
        except Exception as ex:
            raise AuthSetServiceException("(putTargetFile method)->{0}".format(ex))

    @staticmethod
    def replacingOperation(autoSetConfig, targetFileData) -> str:
        """
        Replacing all variables which are specified on config to properties.
        :param autoSetConfig: set configuration which is wanted to replace.
        :param targetFileData: target file data
        :return: all data which is replaced.
        """
        try:
            for key_t, value_t in autoSetConfig.items():
                targetFileData = re.sub("{}=.+".format(key_t), "{0}={1}".format(key_t, value_t), targetFileData)

            return targetFileData

        except Exception as ex:
            raise AuthSetServiceException("(replacingOperation method)->{0}".format(ex))

    def run(self):
        """
        The entry point of the service.
        :return void
        """
        self.log.info("Target file <{0}> is reading...".format(self.config.targetFile))
        targetFileData = self.getTargetFile(self.config.targetFile)

        self.log.info("Target file and configuration are matching...")
        targetFileData = self.replacingOperation(self.config.authSet, targetFileData)

        self.log.info("New target file is writing...")
        self.putTargetFile(self.config.targetFile, targetFileData)


