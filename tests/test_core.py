from kott import Kott
from kott.kplugs import KSample
from kott.kplugs import KTag
from kott.kplugs import KString

class Student:
    name = "<unset>"
    grade = "<unset>"

    def __init__(self, _name, _grade):
        self.name = _name
        self.grade = _grade

    def __str__(self):
        return "Name: " + self.name + ", Grade: " + self.grade


print ("---------- Testing Kott ----------")
object_key = Kott().set("Hello Kott!")
object_value = Kott().get(object_key)
print ("Key: " + str(object_key) + ", Value: " + str(object_value))

print ("---------- Testing Sample KPlug ----------")
Kott().load_kplug(KSample())
object_value = Kott().get(object_key, sample_arg="A Sample Argument for GET")
print ("Key: " + str(object_key) + ", Value: " + str(object_value))
object_key = Kott().set("Sample Data", sample_arg="A Sample Argument for SET")
object_value = Kott().get(object_key, sample_arg="A Sample Argument for GET again!")
print ("Key: " + str(object_key) + ", Value: " + str(object_value))
Kott().delete(object_key)

print ("---------- Testing KTags ----------")
Kott().load_kplug(KTag())
Kott().set("Tagged value no.1", tag="Test Tag")
Kott().set("Tagged value no.2", tag="Test Tag")
Kott().set("Tagged value no.3", tag="Test Tag")
result = Kott().find(tag="Test Tag")
for r in result:
    print Kott().get(r)

print ("---------- Testing KStrings ----------")

Kott().load_kplug(KString())
Kott().set(Student("Sina", "F-"))
Kott().set(Student("Mostafa", "F+"))
Kott().set(Student("Sami", "C-"))

print ("--- Test str_equal")
result = Kott().find(str_equal="Tagged value no.3")
for r in result:
    print Kott().get(r)

print ("--- Test str_has")
result = Kott().find(str_has="Grade")
for r in result:
    print Kott().get(r)

print ("--- Test str_regex 1")
result = Kott().find(str_regex=".*F.*")
for r in result:
    print Kott().get(r)

print ("--- Test str_regex 2")
result = Kott().find(str_regex=".*gg\w.*")
for r in result:
    print Kott().get(r)

Kott().cleanup()
