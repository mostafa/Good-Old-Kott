# -*- coding: utf-8 -*-
# TODO: KExceptoin, check data type,
"""docstring."""

from kcore.ksingleton import kSingleton
from kcore import krand
from kplug import KPlugBase
from kcore.kconf import __kott_kplugs_dir__

import md5
import time
import string
import random
import threading
import time
import sys
import os


@kSingleton
class Kott:
    __mem__ = {}
    __kplugs__ = []
    KOTT_UNTAGGED_DATA = "uncategorized_kott_keys"

    def __init__(self):
        pass

    def load_kplug(self, kplug_instance):
        self.__kplugs__.append(kplug_instance)
        self.__kplugs__.sort(lambda x, y: x.priority < y.priority)
        return kplug_instance.on_load()

    def get(self, key, **kwargs):
        value = self.__mem__[key]

        tp = type(value)
        for c_kplug in self.__kplugs__:
            if isinstance(value, c_kplug.data_type):
                value = c_kplug.on_get(key, value, **kwargs)

        return value

    def set(self, data, **kwargs):
        key = md5.md5(krand.kRandStr(16) + str(time.time())).hexdigest()
        for kplug in self.__kplugs__:
            data = kplug.on_set(key, data, **kwargs)
        self.__mem__[key] = data
        return key

    def pop(self, key, **kwargs):
        if key in self.__mem__:
            data = self.get(key, **kwargs)
            self.delete(key, **kwargs)
            return data
        return None

    def find(self, **kwargs):
        found_keys = []
        for key in self.__mem__:
            tp = type(self.__mem__[key])
            for c_kplug in self.__kplugs__:
                if isinstance(self.__mem__[key], c_kplug.data_type):
                    if c_kplug.on_find_visit(key, self.__mem__[key], **kwargs):
                        found_keys.append(key)
        return found_keys

    def delete(self, key, **kwargs):
        if key in self.__mem__:
            self.__mem__.pop(key)

    def cleanup(self, **kwargs):
        self.__mem__ = {}
