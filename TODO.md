# TODO
+ [X] Build a semaphore for __mem__ because of multiple threads modifying singletoned kott object
+ [X] Make you release the semaphore before a "raise"
+ [ ] Add exception handling by the concept of failureaction library: [failureaction 1.0a1](https://pypi.python.org/pypi/failureaction/1.0a1)
+ [ ] Default behavior for exception handling:
    + Production:
        0. Release semaphore
        1. Raise
        2. Log
        3. **Continue**
    + Development:
        0. Release semaphore
        1. Raise
        2. Log
        3. **Break**
+ [ ] Add system-wide and kplug-level configuration of logging and exception handling
+ [ ] Add logging to kcore
+ [X] CRUD: Add Update and OnUpdate methods
+ [X] Add tag to already existing data!
+ [X] find must check for object type
+ [ ] KConf and that freakin idea!
+ [X] use UUID as keys instead of hash functions
+ [ ] KCache
+ [ ] Making a list of core kplugs (e.g. kTag, kGraph, kDHT, ...)
+ [X] TTimer
+ [ ] Add a web interface to manage objects (kAdmin)
+ [ ] KRest
+ [ ] KObjectToDiskSerializator (Persistance & Recovery from crash etc.)
+ [ ] KQueue, a message queue plugin
+ [ ] DHT (DMT)
+ [X] Deceide whether onSet should return value or True/False (on_set returns boolean)
+ [ ] Restful API to manage Kott (Mostafata's version)
+ [X] Add support for finding all base types (str, int, float, double, ...): KPlug
+ [X] Refactor KPlugBase to be singleton (KPlugBase metaclass is kSingleton)

# TODO (with less priorities)
+ [-] Refactor KPlugBase to become a Meta class (abc.ABCMeta) with abstract functions
+ [ ] Factory pattern for initializing Kott objects.
+ [-] KGraph: Redesign (setup a meeting)
