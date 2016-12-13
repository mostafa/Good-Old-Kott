class KPlugBase:
    _data_type_ = object
    _priority_ = 99

    def __init__(self):
        pass

    @property
    def data_type(self):
        return self._data_type_

    @property
    def priority(self):
        return self._priority_

    def on_set(self, key, value, **kwargs):
        return value

    def on_get(self, key, value, **kwargs):
        return value

    def on_load(self):
        return True

    def on_delete(self, key, value, **kwargs):
        pass

    def on_find_visit(self, key, value, **kwargs):
        return False
