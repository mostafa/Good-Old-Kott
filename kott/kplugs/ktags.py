from kott import kplug
from kott.kcore.ksingleton import kSingleton


@kSingleton
class KTags(kplug.KPlugBase):
    __tag__ = {}
    KOTT_UNTAGGED_DATA = "uncategorized_kott_keys"

    def __init__(self):
        _priority_ = 10

    def on_set(self, key, value, **kwargs):
        if "tag" in kwargs:
            print ("Setting tag:" + kwargs["tag"] +
                   " for key:" + key + ", value: " + value)
            if kwargs["tag"] in self.__tag__:
                self.__tag__[kwargs["tag"]].append(key)
            else:
                self.__tag__[kwargs["tag"]] = [key]
        return value

    def on_find_visit(self, key, value, **kwargs):
        if "tag" in kwargs:
            if kwargs["tag"] in self.__tag__:
                if key in self.__tag__[kwargs["tag"]]:
                    print ("Found tag:" + kwargs["tag"] +
                           " on key:" + key + ", value: " + value)
                    return True
            return False
        return False
