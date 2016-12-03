# -*- coding: utf-8 -*-
"""docstring."""

from kcore.ksingleton import kSingleton
from kcore import krand
from kplug import KPlugBase

import md5
import time
import string
import random
import threading
import time

@kSingleton
class Kott:
    __mem__ = None
    __tag__ = None
    # __write_semaphore__ = asyncio.Lock()

    KOTT_UNTAGGED_DATA = "uncategorized_kott_keys"

    def __init__(self):
        self.__mem__ = {}
        self.__tag__ = {}

    def get(self, key):
        return self.__mem__[key]

    def get_tagged_keys(self, tag):
        if tag in self.__tag__:
            return self.__tag__[tag]
        return None

    def set(self, data, tag = KOTT_UNTAGGED_DATA):
        key = md5.md5(krand.kRandStr(16) + str(time.time())).hexdigest()
        self.__mem__[key] = data
        if tag in self.__tag__:
            self.__tag__[tag].append(key)
        else:
            self.__tag__[tag] = [key]
        return key

    def pop(self, key):
        if key in self.__mem__:
            return self.__mem__.pop(key)
        return None

    def cleanup(self):
        self.__mem__ = {}

# print (type(Kott))
# k = Kott().set("blah blah")
# print Kott().get(k)
# print Kott().pop(k)
