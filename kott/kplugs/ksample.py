from kott.kplugbase import KPlugBase
from kott.kcore.ksingleton import kSingleton

from kott.kcore import krand
@kSingleton
class KSample(KPlugBase):
    _keywords_ = ["sample_arg"]

    some_shared_data = "Singleton Shared Data " + krand.kRandStr(4)

    def on_load(self):
        print ("KSample is up! (" + self.some_shared_data + ")")

    def on_get(self, key, value, **kwargs):
        print ("KSample on_get(" + kwargs["sample_arg"] + ")! (" + self.some_shared_data + ")")
        return value

    def on_set(self, key, value, **kwargs):
        print ("KSample on_get(" + kwargs["sample_arg"] + ")! (" + self.some_shared_data + ")")
        return value
