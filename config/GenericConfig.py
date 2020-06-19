"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""


class GenericConfig:
    def __init__(self,
                 appTargetFile: str = None,
                 appRunScript: str = None,
                 baseDir: str = None,
                 startUpCommand: str = None,
                 javaPath: str = None
                 ):
        self.appTargetFile = appTargetFile
        self.appRunScript = appRunScript
        self.baseDir = baseDir
        self.startUpCommand = startUpCommand
        self.javaPath = javaPath
