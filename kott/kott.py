# -*- coding: utf-8 -*-
# TODO: KExceptoin, check data type,
"""docstring."""

from kcore.ksingleton import kSingleton
from kcore import krand
from kplugbase import KPlugBase
from kcore.kconf import __kplug_do_prefix__

import md5
import time
import string
import random
import threading
import time
import sys
import os


class Kott:
    __metaclass__ = kSingleton
    __mem__ = {}
    __kplugs__ = []

    def __init__(self):
        pass

    def load_kplug(self, kplug_instance):
        self.__kplugs__.append(kplug_instance)
        self.__kplugs__.sort(lambda x, y: x.priority < y.priority)
        return kplug_instance.on_load()

    def get(self, key, **kwargs):
        value = self.__mem__[key]

        for c_kplug in self.__kplugs__:
            if isinstance(value, c_kplug.data_type) and \
               c_kplug.has_keyword(**kwargs):
                value = c_kplug.on_get(key, value, **kwargs)

        return value

    def set(self, data, **kwargs):
        key = md5.md5(krand.kRandStr(16) + str(time.time())).hexdigest()
        for c_kplug in self.__kplugs__:
            if isinstance(data, c_kplug.data_type) and \
               c_kplug.has_keyword(**kwargs):
                data = c_kplug.on_set(key, data, **kwargs)
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
        # print self.__kplugs__
        # print kwargs

        for key in self.__mem__:
            kplug_res = {}
            for c_kplug in self.__kplugs__:
                kplug_res[c_kplug] = True
                # print c_kplug.has_keyword(**kwargs)
                if isinstance(self.__mem__[key], c_kplug.data_type) and \
                   c_kplug.has_keyword(**kwargs):
                    kplug_res[c_kplug] = c_kplug.on_find_visit(key, self.__mem__[key], **kwargs)

            # print kplug_res
            and_all = True
            for plug in kplug_res:
                and_all = and_all and kplug_res[plug]
            if and_all and len(kplug_res) > 0:
                found_keys.append(key)

        return found_keys

    def do(self, *args, **kwargs):
        do_keys = self.find(**kwargs)
        # print (do_keys)

        for c_kplug in self.__kplugs__:
            for method in args:
                try:
                    func = getattr(c_kplug, __kplug_do_prefix__ + method)
                    # print (func)
                    for key in do_keys:
                        func(key, self.__mem__[key], **kwargs)
                except Exception as e:
                    # print ("method is not there")
                    pass
            # end of for method
        # end of for kplugs

    def delete(self, key, **kwargs):
        if key in self.__mem__:
            value = self.__mem__[key]

            for c_kplug in self.__kplugs__:
                if isinstance(value, c_kplug.data_type) and \
                   c_kplug.has_keyword(**kwargs):
                    value = c_kplug.on_delete(key, value, **kwargs)
            del self.__mem__[key]

    def cleanup(self, **kwargs):
        for key in self.__mem__.keys():
            self.delete(key, **kwargs)
