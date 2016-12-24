from kott import Kott

# instantiate a singleton object of the Kott class
# so that it can be accessed like this:
# Kott.set("test data") instead of Kott().set("test data")
# TODO: There should be a better way to implement this!
Kott = Kott()