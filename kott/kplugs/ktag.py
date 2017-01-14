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
        if kwargs["tag"] in self.__tag__:
            self.__tag__[kwargs["tag"]].append(key)
        else:
            self.__tag__[kwargs["tag"]] = [key]

        return value

    def on_find_visit(self, key, value, **kwargs):
        if kwargs["tag"] in self.__tag__:
            if key in self.__tag__[kwargs["tag"]]:
                # TODO: KLog
                # print ("Found tag:" + kwargs["tag"] +
                #        " on key:" + str(key) + ", value: " + str(value))
                return True
        return False
