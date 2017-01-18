"""
   KTimerPool
"""


from kott.kplugbase import KPlugBase
from kott.kplugs import KTag

import threading
import traceback
import sys
import os.path


class KTimerPool(KTag):
    _priority_ = 9
    _data_type_ = threading.Timer
    _keywords_ = ["pool", "is_alive"]

    def on_set(self, key, value, **kwargs):
        return super().on_set(key, value, **dict(kwargs, tag=kwargs["pool"]))

    def on_find_visit(self, key, value, **kwargs):
        alive = True

        if "is_alive" in kwargs and kwargs["is_alive"]:
            alive = value.isAlive()

        return alive and super().on_find_visit(key, value, **dict(kwargs, tag=kwargs["pool"]))

    def kplug_do_find_alives(self, key, value, **kwargs):
        return value.isAlive()

    def kplug_do_start(self, key, value, **kwargs):
        value.start()

    def kplug_do_kill(self, key, value, **kwargs):
        value.cancel()

    def create_timer(thread_timeout,
                     thread_callback,
                     *thread_args,
                     **thread_kwargs):
        return threading.Timer(thread_timeout,
                               thread_callback,
                               *thread_args,
                               **thread_kwargs)
