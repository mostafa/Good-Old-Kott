# import inspect
from .kcore.ksingleton import kSingleton


class KPlugBase(object):
    __metaclass__ = kSingleton
    _data_type_ = object
    _priority_ = 99
    _keywords_ = []

    def __init__(self):
        pass

    @property
    def data_type(self):
        return self._data_type_

    @property
    def priority(self):
        return self._priority_

    @property
    def keywords(self):
        return self._keywords_

    def has_keyword(self, **kwargs):
        # print self._keywords_
        # print kwargs
        for k in self._keywords_:
            if k in kwargs:
                return True
        return False

    def on_set(self, key, value, **kwargs):
        return True

    def on_get(self, key, value, **kwargs):
        return value

    def on_load(self):
        return True

    def on_delete(self, key, value, **kwargs):
        pass

    def on_find_visit(self, key, value, **kwargs):
        return False
