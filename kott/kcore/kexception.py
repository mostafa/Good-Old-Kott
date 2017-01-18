# -*- coding: utf-8 -*-
"""Exception handling decorator for functions and methods"""

# import sys
# import traceback
from .kconf import __exception_prefix__


class kException(BaseException):

    """
        Base class for all exceptions raised in Kott
    """

    def __init__(self, message):
        BaseException.__init__(self, message)
        self.message = message

    def __str__(self):
        return __exception_prefix__ + self.message


class InvalidKeyword(kException):

    """
        Exception: An invalid keyword argument (**kwargs) is passed to a method
    """

    def __init__(self, keyword):
        self.message = "Keyword does not exist: " + str(keyword)


class InvalidKey(kException):

    """
        Exception: Requested key does not exist in Kott memory
    """

    def __init__(self, key):
        self.message = "Key does not exist: " + str(key)


class KPlugOnSetError(kException):

    """
        Exception: An error occurred when setting an item on a KPlug
    """

    def __init__(self, key, kplug_name):
        self.message = "Cannot set item [" + key + \
            "] on KPlug: " + kplug_name


class KPlugOnGetError(kException):

    """
        Exception: An error occurred when getting an item from a KPlug
    """

    def __init__(self, key, kplug_name):
        self.message = "Cannot get item [" + key + \
            "] from KPlug: " + kplug_name


class InvalidNumberOfArguments(kException):

    """
        Exception: Invalid number of arguments passed to method
    """

    def __init__(self, func_name, total, arg_len):
        self.message = "Invalid number of arguments passed to method:" + \
            func_name + ". Expected: " + total + " Passed: " + arg_len
