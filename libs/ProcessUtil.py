"""
Author: Software Engineer Muhammet Bolat
Copyright (C): 2020 Muhammet Bolat
Licence: Public Domain
"""
import psutil as ps


class ProcessUtil:
    """
    THIS IS NOT DESCRIPTION FOR "ProcessUtil.py" CLASS.
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
    def allRunningProcess():
        """
        The method gets all running process
        :return: all process as list
        """
        allRunningProcess = list()

        for proc in ps.process_iter():
            try:
                allRunningProcess.append(proc)
            except ps.NoSuchProcess as ex:
                raise SystemError("No process is found -> {}".format(ex))

            except ps.AccessDenied as ex:
                raise SystemError("Access Denied for showing process -> {}".format(ex))

            except Exception as ex:
                raise SystemError("Undefined error -> {}".format(ex))

        return allRunningProcess

    @staticmethod
    def findProcByName(processName):
        """
        The method finds out process with given process name.
        i.e java, python3.7
        :param processName: name of the process
        :return: list of the process which is found.
        """
        filterProcessList = list()

        for proc in ProcessUtil.allRunningProcess():
            if proc.name() == processName:
                filterProcessList.append(proc)

        return filterProcessList

    @staticmethod
    def findProcByCommandLineArgs(commandLine):
        """
        The method finds out process with given commamnd line args.
        i.e /usr/bin/python ProcessUtil.py
        :param commandLine: commandLine arguman. i.e ProcessUtil.py
        :return: list of process.
        """
        filterProcess = set()
        for proc in ProcessUtil.allRunningProcess():
            try:
                cmdLineList = ps.Process(proc.pid).cmdline()
                for cmd in cmdLineList:
                    if commandLine in cmd:
                        filterProcess.add(proc)
            except (ps.NoSuchProcess, ps.AccessDenied, ps.ZombieProcess):
                pass

        return filterProcess

    @staticmethod
    def killProcess(proc):
        """
        The method kill process.
        :param proc: object of the Process
        :return: Boolean. If the process is kill, returns True(Success), otherwise False(Fail)
        """
        try:
            return proc.kill()
        except ps.NoSuchProcess as ex:
            raise SystemError("No process is found -> {}".format(ex))
        except ps.AccessDenied as ex:
            raise SystemError("Access Denied for showing process -> {}".format(ex))
        except Exception as ex:
            raise SystemError("Undefined error -> {}".format(ex))












