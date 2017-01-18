"""
    KTag
"""

from kott.kplugbase import KPlugBase


class KTag(KPlugBase):
    _priority_ = 1
    __tag__ = {}
    _keywords_ = ["tag"]
    KOTT_UNTAGGED_DATA = "uncategorized_kott_keys"

    def __init__(self):
        self._priority_ = 1

    def on_set(self, key, value, **kwargs):
        # TODO: KLog
        # print ("Setting tag:" + kwargs["tag"] +
        #        " for key:" + str(key) + ", value: " + str(value))
        found_tag = None
        for tag, key_list in self.__tag__.items():
            for current_key in key_list:
                if current_key == key:
                    found_tag = tag
                    break

        if (found_tag is not None):
            self.__tag__[found_tag].remove(key)

        if kwargs["tag"] in self.__tag__:
            self.__tag__[kwargs["tag"]].append(key)
        else:
            self.__tag__[kwargs["tag"]] = [key]

        return True

    def on_find_visit(self, key, value, **kwargs):
        if kwargs["tag"] in self.__tag__:
            if key in self.__tag__[kwargs["tag"]]:
                # TODO: KLog
                # print ("Found tag:" + kwargs["tag"] +
                #        " on key:" + str(key) + ", value: " + str(value))
                return True
        return False
