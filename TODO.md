# TODO
+ [X] Build a semaphore for __mem__ because of multiple threads modifying singletoned kott object
+ [ ] Add exception handling by the concept of failureaction library: [failureaction 1.0a1](https://pypi.python.org/pypi/failureaction/1.0a1)
+ [ ] Default behavior for exception handling:
    + Production:
        1. Raise
        2. Log
        3. **Continue**
    + Development:
        1. Raise
        2. Log
        3. **Break**
+ [ ] Add system-wide and kplug-level configuration of logging and exception handling
+ [ ] Add logging to kcore
+ [X] CRUD: Add Update and OnUpdate methods
+ [X] Add tag to already existing data!
+ [X] find must check for object type
+ [ ] kConf and that freakin idea!
+ [X] use UUID as keys instead of hash functions
+ [-] kGraph
+ [ ] kCache
+ [ ] Making a list of core kplugs (e.g. kTag, kGraph, kDHT, ...)
+ [ ] Add a web interface to manage objects (kAdmin)
+ [ ] kRest
+ [ ] kObjectToDiskSerializator (Persistance & Recovery from crash etc.)
+ [ ] kQueue, a message queue plugin
+ [ ] DHT (DMT)
+ [X] Deceide whether onSet should return value or True/False (on_set returns boolean)
+ [ ] Restful API to manage Kott (Mostafata's version)
+ [X] Add support for finding all base types (str, int, float, double, ...): KPlug
+ [X] Refactor KPlugBase to be singleton (KPlugBase metaclass is kSingleton)

# TODO (with less priorities)
+ [-] Refactor KPlugBase to become a Meta class (abc.ABCMeta) with abstract functions
+ [ ] Factory pattern for initializing Kott objects.
