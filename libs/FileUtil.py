"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""
import yaml


class FileUtil:
    """
    THIS IS NOT DESCRIPTION FOR "FileUtil.py" CLASS.
    This part represent to Static Initializer Code on Java, it's check to version for the available version.
    At least current Python version must be 3.7.0+, anything else you should update Python version
    """

    def __init__(self):
        """
        INFO: Default Constructor cannot be Creatable
        WARNING: If attend to create this object, it will raise NotImplementedError
        """
        assert NotImplementedError("This object using only library, cannot be creatable!!!")

    def __new__(cls):
        """
        INFO: This method was overrided only avoided to __new__ operator
        :return: NOISE_OBJECT
        """
        return object.__new__(cls)

    @staticmethod
    def readFile(filename) -> str:
        """
        This method reads given file. It returns all datas as str(string) data structure.
        :param filename: absolute path of the given file
        :return: file datas as str.
        """
        with open(filename) as f:
            file = f.read()
        return file

    @staticmethod
    def readFileAsList(filename):
        """
        This method reads given file. It returns all datas as list data structure.
        :param filename: absolute path of the given file
        :return: file datas as list.
        """
        return FileUtil.readFile(filename).split('/n')

    @staticmethod
    def readYaml(filename):
        """
        This method reads YAML file. It returns all datas as dictionary data structure.
        :param filename: absolute path of the given file
        :return: file datas as dict.
        """
        with open(filename, 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return cfg

    @staticmethod
    def writeFile(filename, data):
        """
        This method write datas into given file.
        :param filename: absolute path of the given file
        :param data: string data which is claimed tow write a file.
        :return:
        """
        with open(filename, 'w') as f:
            f.write(data)
