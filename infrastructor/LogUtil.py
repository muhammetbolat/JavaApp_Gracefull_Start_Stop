"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""
import logging
import os
from datetime import datetime

from config.LoggerConfig import LoggerConfig


class Logger:
    def __init__(self,
                 logConfig: LoggerConfig = None,
                 logLevel: int = logging.DEBUG,
                 logFormat: str = "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s",
                 logDateFormat: logging.Formatter = '%Y-%m-%d %H:%M:%S',
                 fileMode: str = 'a'
                 ):
        self.logAppHeader = logConfig.logAppHeader
        self.logPath = logConfig.logPath
        self.logFileName = logConfig.logFileName

        self.logLevel = logLevel
        self.logFormat = logFormat
        self.logDateFormat = logDateFormat
        self.fileMode = fileMode

        self.log = None

        self.__checkLogPath()
        self.__setLogConfig()

    def __checkLogPath(self):
        """
        This method helps to user avoid exception as 'file doesnt exist'.
        :return: nothing.
        """
        if os.path.exists(self.logPath):
            return

        os.mkdir(self.logPath)

    def __setLogConfig(self):
        # create logger with logAppHeader
        self.log = logging.getLogger(self.logAppHeader)
        self.log.setLevel(self.logLevel)

        # create file handler which logs even debug messageasdzxc.1
        # s
        print("For more detail... -> {0}".format(os.path.join(self.logPath, self.logFileName.format(datetime.now()))))
        fh = logging.FileHandler(os.path.join(self.logPath, self.logFileName.format(datetime.now())))
        fh.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # create formatter and add it to the handlers
        fh.setFormatter(logging.Formatter(self.logFormat))
        ch.setFormatter(logging.Formatter(self.logFormat))
        # add the handlers to the log object
        self.log.addHandler(fh)
        self.log.addHandler(ch)

