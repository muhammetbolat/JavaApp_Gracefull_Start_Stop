"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""


class DataBaseConfig:
    def __init__(self,
                 host: str = None,
                 port: int = None,
                 dbName: str = None,
                 userName: str = None,
                 password: str = None):
        self.host = host
        self.port = port
        self.dbName = dbName
        self.userName = userName
        self.password = password
