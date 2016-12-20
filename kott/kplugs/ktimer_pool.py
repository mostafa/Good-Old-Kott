from kott.kplugbase import KPlugBase

import threading
import traceback
import sys
import os.path

class KTimerPool(KPlugBase):
    _data_type_ = threading.Timer
    _keywords_ = ["is_alive"]

    def on_find_visit(self, key, value, **kwargs):
        return value.isAlive() == kwargs["is_alive"]

    def kplug_do_start(self, key, value, **kwargs):
        value.start()

    def kplug_do_kill(self, key, value, **kwargs):
        value.cancel()
