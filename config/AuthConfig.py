"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""


class AuthConfig:
    def __init__(self,
                 targetFile: str = None,
                 authSet: dict = None):
        self.targetFile = targetFile
        self.authSet = authSet

