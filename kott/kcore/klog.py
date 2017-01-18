# -*- coding: utf-8 -*-

from functools import wraps
from time import time


"""
Used as a decorator, it can calculate the time it takes
for a method or function to complete.
reference: http://stackoverflow.com/a/27737385
"""


def kCalcDiffTime(function):
    @wraps(function)
    def wrap(*args, **kw):
        ts = time()
        result = function(*args, **kw)
        te = time()
        print('function:%r arguments:[%r, %r] took: %2.4f sec' %
              (function.__name__, args, kw, te - ts))
        return result
    return wrap
