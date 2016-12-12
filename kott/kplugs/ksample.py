from kott import kplug
from kott.kcore.ksingleton import kSingleton

from kott.kcore import krand
@kSingleton
class KSample( kplug.KPlugBase ):
    some_shared_data = "Singleton Shared Data " + krand.kRandStr(4)

    def on_load(self):
        print ("KSample is up! (" + self.some_shared_data + ")")

    def on_get(self, key, value, **kargs):
        print ("KSample on_get(" + kargs["sample_arg"] + ")! (" + self.some_shared_data + ")")
        return value

    def on_set(self, key, value, **kargs):
        print ("KSample on_get(" + kargs["sample_arg"] + ")! (" + self.some_shared_data + ")")
        return value
