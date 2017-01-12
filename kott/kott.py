#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Kott - an abstract data store
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Kott is an abstract data store, where you can store anything
    and retrieve it easily. Our motto is `One Kott fits all!`.
    The whole idea is around the concept of a key-value store, but
    has been abstracted to a level that can accept any form, model or
    data. This means literally everything. Kott is singleton, so there
    exists only a single instance of it.

    >>> from kott import Kott
    >>> id = Kott().set("my test data which is a string!")
    >>> len(id)
    32
    >>> type(id)
    <type 'str'>
    >>> Kott().get(id)
    'my test data which is a string!'

    As you can see, there is almost no need for storing the keys or
    saving them somewhere, because you can always find your data.
    For example, you can store the instances of your classes in Kott
    and later access them using their keys. The magic happens with
    the concept and implementation of Kott plugins or KPlugs.
    Everything beyond the concept of key-value store is written
    as kplug. There are official (bundled) kplugs, such as KTag,
    KTimerPool, KString, ... . Every kplug adds its own keywords
    to the core of Kott. So, if you want to tag your data while
    inserting it into Kott, you just use the keyword `tag` as follows.
    KPlugs are also singleton, and they have priorities while running,
    so, a kplug with a lower value is executed before a kplug with a
    higher value. To demonstrate the power and flexibility of Kott,
    have a look at the example below. Official kplugs are called and
    loaded by their name as string, but custom kplugs (written by users)
    should be passed as instance.

    >>> Kott().load_kplug("KTag")  # True if loaded, False otherwise
    True
    >>> Kott().set(123, tag="my_numbers")
    >>> Kott().set(456, tag="my_numbers")
    >>> Kott().set(789, tag="my_numbers")
    >>> ids = Kott().find(tag="my_numbers")
    >>> for id in ids:
    ...     Kott().get(id)
    123
    456
    789

    The find method looks for keywords in each kplug, and starts searching
    one by one to find the matching value, then it returns their IDs.

    A sample kplug, KSample, is provided as an example for kplug developers.

    :copyright: (c) 2016 by Hossein Ghannad, Sina Hatefmatbue, Mostafa Moradian
    :license: TBD, see LICENSE for more details.
"""

from .kcore.ksingleton import kSingleton
# from .kcore import krand
from .kcore.ktime import kTime
from .kcore.kconf import __kplug_do_prefix__

import uuid
import time


class Kott:
    __metaclass__ = kSingleton
    __mem__ = {}
    __kplugs__ = []

    def __init__(self):
        pass

    def load_kplug(self, kplug_name_or_instance):
        kplug_instance = None

        if (isinstance(kplug_name_or_instance, str)):
            try:
                import importlib
                kplug_module = importlib.import_module(
                    "kott.kplugs", kplug_name_or_instance)
                kplug_instance = getattr(
                    kplug_module, kplug_name_or_instance)()
            except Exception as e:
                raise e
        else:
            kplug_instance = kplug_name_or_instance

        if kplug_instance is None:
            return False

        self.__kplugs__.append(kplug_instance)
        self.__kplugs__.sort(key=lambda obj: obj.priority)
        return kplug_instance.on_load()

    def get(self, key, **kwargs):
        value = self.__mem__[key]

        for c_kplug in self.__kplugs__:
            if isinstance(value, c_kplug.data_type) and \
               c_kplug.has_keyword(**kwargs):
                value = c_kplug.on_get(key, value, **kwargs)

        return value

    def set(self, data, **kwargs):
        key = uuid.uuid1().hex
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

    # For testing purposes, time diff is calculated!
    # @kTime
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
                    kplug_res[c_kplug] = c_kplug.on_find_visit(
                        key, self.__mem__[key], **kwargs)

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
        for key in list(self.__mem__):
            self.delete(key, **kwargs)


# Doctest does not work correctly, because of relative imports in code
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)

# instantiate a singleton object of the Kott class
# so that it can be accessed like this:
# Kott.set("test data") instead of Kott().set("test data")
# TODO: There should be a better way to implement this!
Kott = Kott()
