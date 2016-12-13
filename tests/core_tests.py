from kott import Kott
from kott.kplugs import ksample
from kott.kplugs import ktags

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

print ("---------- Testing KTag ----------")
Kott().load_kplug(ktags.KTags())
Kott().set("Tagged value no.1", tag="Test Tag")
Kott().set("Tagged value no.2", tag="Test Tag")
Kott().set("Tagged value no.3", tag="Test Tag")
result = Kott().find(tag="Test Tag")
for r in result:
    print Kott().get(r)
