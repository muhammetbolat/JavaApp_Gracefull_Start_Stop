"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""


class StopAppConfig:
    def __init__(self,
                 stopAllRouteID: str = None,
                 routeTableCheckInterval: str = None):
        self.stopAllRouteID = stopAllRouteID
        self.routeTableCheckInterval = routeTableCheckInterval
