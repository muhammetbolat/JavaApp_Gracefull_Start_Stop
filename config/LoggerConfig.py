"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""


class LoggerConfig:
    def __init__(self,
                 logAppHeader: str = "",
                 logPath: str = None,
                 logFileName: str = None
                 ) -> None:
        self.logAppHeader = logAppHeader
        self.logPath = logPath
        self.logFileName = logFileName



