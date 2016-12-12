from kott import kplug
from kott.kcore.ksingleton import kSingleton

@kSingleton
class KTags( kplug.KPlugBase ):
    __tags__ = {}
    KOTT_UNTAGGED_DATA = "uncategorized_kott_keys"
    # TODO
