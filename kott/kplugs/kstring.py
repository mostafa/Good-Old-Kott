from kott.kplugbase import KPlugBase
import re

class KString(KPlugBase):
    _priority_ = 0
    _keywords_ = ["str_equal", "str_has", "str_regex"]

    def __init__(self):
        _priority_ = 1

    def on_find_visit(self, key, value, **kwargs):
        if hasattr(value, "__str__"):
            # print ("match against " + str(value))
            if "str_equal" in kwargs:
                return str(value) == kwargs["str_equal"]
            elif "str_has" in kwargs:
                return kwargs["str_has"] in str(value)
            elif "str_regex" in kwargs:
                p = re.compile(kwargs["str_regex"])
                return p.search(str(value)) is not None

        return False
