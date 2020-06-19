"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""


class SqlConfig:
    def __init__(self,
                 routesSelectQuery: str = None,
                 stopAllRoutesInsert: str = None,
                 stopAllRoutesDelete: str = None,
                 criticalRoutesStopCheck: str = None,
                 updateRoutesStopInformation: str = None):

        self.routesSelectQuery = routesSelectQuery
        self.stopAllRoutesInsert = stopAllRoutesInsert
        self.stopAllRoutesDelete = stopAllRoutesDelete
        self.criticalRoutesStopCheck = criticalRoutesStopCheck
        self.updateRoutesStopInformation = updateRoutesStopInformation
