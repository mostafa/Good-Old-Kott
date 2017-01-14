# TODO
+ [ ] Lazy-load kplugs based on used keyword
+ [ ] Add exception handling by the concept of failureaction library: (failureaction 1.0a1)[https://pypi.python.org/pypi/failureaction/1.0a1]
+ [ ] Add system-wide and kplug-level configuration of logging and exception handling
+ [ ] Add logging to kcore
+ [ ] Add tag to already existing data!
+ [ ] Add a web interface to manage objects (kAdmin)
+ [ ] Build a semaphore for mem because of multi threads modifying singletoned kott object
+ [ ] CRUD: Add Update and OnUpdate methods
+ [ ] find must check for object type
+ [ ] kConf and that freakin idea!
+ [ ] use UUID as keys instead of hash functions
+ [ ] kGraph
+ [ ] kCache
+ [ ] Making a list of core kplugs
+ [ ] kRest
+ [ ] kObjectToDiskSerializator (Persistance & Recovery from crash etc.)
+ [ ] kQueue, a message queue plugin
+ [ ] DHT (DMT)
+ [ ] Deceide whether onSet should return value or True/False
+ [ ] Restful API to manage Kott (Mostafata's version)
+ [X] Add support for finding all base types (str, int, float, double, ...): KPlug
+ [X] Refactor KPlugBase to be singleton (KPlugBase metaclass is kSingleton)

# TODO (with less priorities)
+ [ ] Refactor KPlugBase to become a Meta class (abc.ABCMeta) with abstract functions
+ [ ] Proxy pattern for initializing Kott objects.
