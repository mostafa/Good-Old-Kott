from kott import Kott
from kott.kplugs import ksample

print ("---------- Testing Kott ----------")
object_key = Kott().set("Hello Kott!")
object_value = Kott().get(object_key)
print ("Key: " + str(object_key) + ", Value: " + str(object_value))

print ("---------- Testing Sample KPlug ----------")
Kott().load_kplug(ksample.KSample())
object_value = Kott().get(object_key, sample_arg="A Sample Argument for GET")
print ("Key: " + str(object_key) + ", Value: " + str(object_value))
object_key = Kott().set("Sample Data", sample_arg="A Sample Argument for SET")
object_value = Kott().get(object_key, sample_arg="A Sample Argument for GET again!")
print ("Key: " + str(object_key) + ", Value: " + str(object_value))
