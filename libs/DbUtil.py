"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""
import cx_Oracle as db
from config.DataBaseConfig import DataBaseConfig


class Oracle:
    """
    THIS IS NOT DESCRIPTION FOR "DbUtil.py" CLASS.
    This part represent to Static Initializer Code on Java, it's check to version for the available version.
    At least current Python version must be 3.7.0+, anything else you should update Python version
    """

    def __init__(self,
                 dbConf: DataBaseConfig = None):
        """
        The constructor initialize variables and call connection method.
        :param dbConf: DataBaseConfig object is injected.
        """
        self.__host = dbConf.host
        self.__port = dbConf.port
        self.__dbName = dbConf.dbName
        self.__username = dbConf.userName
        self.__password = dbConf.password
        self.__connectionString = "{0}/{1}@{2}:{3}/{4}".\
            format(self.__username, self.__password, self.__host, self.__port, self.__dbName)
        self.__cursor = None
        self.__con = None

        self.__connect()

    def __connect(self):
        """
        This private method connects to DB.
        :return: nothing
        """
        try:
            self.__con = db.connect(self.__connectionString)
            self.__con.commit()
            self.__cursor = self.__con.cursor()
        except Exception as ex:
            raise ConnectionError("Error occur during the connecting DBMS -> {}".format(str(ex)))

    def query(self, script) -> dict:
        """
        The method send a sql query to DB.
        :param script: SQL Query
        :return: result of the query as dict.
        """
        try:
            self.__cursor.execute(script)
            return self.__cursor.fetchall()
        except Exception as ex:
            raise ConnectionError("Error is occurred in insert method -> {}".format(str(ex)))

    def insert(self, insertScript: str):
        """
        The method insert a data which is given as input.
        :param insertScript: insert sql script
        :return: nothing
        """
        try:
            self.__cursor.execute(insertScript)
            self.__con.commit()
        except Exception as ex:
            raise ConnectionError("Error is occurred in insert method -> {}".format(str(ex)))

    def update(self, updateScript):
        """
        The method update a data which is given as input.
        :param updateScript: update sql script
        :return: nothing
        """
        try:
            self.__cursor.execute(updateScript)
            self.__con.commit()
        except Exception as ex:
            raise ConnectionError("Error is occurred in update method -> {}".format(str(ex)))

    def delete(self, deleteScript):
        """
        The method update a data which is given as input.
        :param deleteScript: update sql script
        :return: nothing
        """
        try:
            self.__cursor.execute(deleteScript)
            self.__con.commit()
        except Exception as ex:
            raise ConnectionError("Error is occurred in delete method -> {}".format(str(ex)))
