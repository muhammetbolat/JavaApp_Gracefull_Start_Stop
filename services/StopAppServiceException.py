"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""


class StopAppServiceException(Exception):
    """
    StopAppService class custom exception.
    """
    def __init__(self, *args):
        if args:
            self.messages = args[0]
        else:
            self.messages = None

    def __str__(self):
        if self.messages:
            return 'StopAppServiceException {0} '.format(self.messages)
        else:
            return 'StopAppServiceException has been raised'
