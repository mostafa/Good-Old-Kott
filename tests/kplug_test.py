from kott import Kott
from kott.kplugbase import KPlugBase
from kott.kplugs import ksample
from kott.kplugs import ktags
from kott.kcore.ksingleton import kSingleton

class Student:
    name = "<unset>"
    grade = "<unset>"

    def __init__(self, _name, _grade):
        self.name = _name
        self.grade = _grade

    def __str__(self):
        return "Name: " + self.name + ", Grade: " + self.grade

@kSingleton
class KStudent(KPlugBase):
    _data_type_ = Student

    def on_find_visit(self, key, value, **kwargs):
        if "name" in kwargs:
            if value.name == kwargs["name"]:
                return True
        return False

Kott().load_kplug(KStudent())
Kott().load_kplug(ktags.KTags())
Kott().set("Hello Kotto!")

s1 = Student("Sina", "F-")
s2 = Student("Mostafa", "F+")
s3 = Student("Sami", "C-")

Kott().set(s1, tag="Coder")
Kott().set(s2, tag="Coder")
Kott().set(s3, tag="Coder")

print ("Finding Sina...")
res = Kott().find(name="Sina")
for r in res:
    print Kott().get(r)

print ("\nFinding Coders...")
res = Kott().find(tag="Coder")
for r in res:
    print Kott().get(r)
