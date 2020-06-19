"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""
import re
import os
import logging as log


class CommonUtil:
    """
    THIS IS NOT DESCRIPTION FOR "CommonUtil.py" CLASS.
    This part represent to Static Initializer Code on Java, it's check to version for the available version.
    At least current Python version must be 3.7.0+, anything else you should update Python version
    """
    def __init__(self):
        """
        INFO: Default Constructure cannot be Creatable
        WARNING: If attand to create this object, it will raise NotImplementedError
        """
        assert NotImplementedError("This object using only library, cannot be creatable!!!")

    def __new__(cls):
        """
        INFO: This method was overrided only avoided to __new__ operator
        :return: NOISE_OBJECT
        """
        return object.__new__(cls)

    @staticmethod
    def equal(s1, s2):
        """
        This method check two values as string and return True or False
        :param s1: First input
        :param s2: Second input
        :return: True if two input are equal or not.
        """
        return s1.strip().lower() == s2.strip().lower()

    ########################################################################################################
    @staticmethod
    def lowerWithoutTurkish(str):
        """
        This method convert Turkish unicode char to ascii
        :param str: input unicode string
        :return: output unicode string
        """
        rep = [('İ', 'I'), ('Ğ', 'G'), ('Ü', 'U'), ('Ş', 'S'), ('Ö', 'O'), ('Ç', 'C'),
               ('ı', 'i'), ('ğ', 'g'), ('ü', 'u'), ('ş', 's'), ('ö', 'o'), ('ç', 'c')]
        for search, replace in rep:
            str = str.replace(search, replace)
        return str

    @staticmethod
    def getFileAsString(path, filename="nodeInfo.txt"):
        textInfo = open(path + filename)
        return textInfo.read()

    @staticmethod
    def getFileAsList(path, filename):
        return re.split('\n', CommonUtil.getFileAsString(path, filename))

    @staticmethod
    def searchFile(path, filename):
        lastFileName = ""
        for fileInPath in os.listdir(path):
            if filename in fileInPath:
                lastFileName = fileInPath
        return CommonUtil.getFileAsList(path, lastFileName)

    @staticmethod
    def log_init(log_file):
        log.basicConfig(filename=log_file,
                        filemode='a',
                        format='%(asctime)s [%(levelname)s] - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=log.DEBUG)
        return log


