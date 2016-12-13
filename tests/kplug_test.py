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

# class Teacher:
#     teacher_name = "<unset>"
#     teacher_students = []
#
#     def __init__(self, _name):
#         self.teacher_name = _name
#
#     def __str__(self):
#         return "Teacher: " + self.name + ", Students: " + len(self.teacher_students)


@kSingleton
class KStudent(KPlugBase):
    _data_type_ = Student
    _keywords_ = ["name"]

    def on_find_visit(self, key, value, **kwargs):
        if "name" in kwargs:
            if value.name == kwargs["name"]:
                return True
            return False
        return True

# @kSingleton
# class KTeacher(KPlugBase):
#     _data_type_ = Teacher
#
#     def on_set(self, key, value, **kwargs):
#         pass

Kott().load_kplug(KStudent())
Kott().load_kplug(ktags.KTags())
Kott().set("Hello Kotto!")
Kott().set("Wuzzup Kotto?")
Kott().set("Bad Kotto!!!", tag="bad")

s1 = Student("Sina", "F-")
s2 = Student("Mostafa", "F+")
s3 = Student("Sami", "C-")

Kott().set(s1, tag="Koder")
Kott().set(s2, tag="Koder")
Kott().set(s3, tag="Koder")

print ("\nFinding the bad...")
res = Kott().find(tag="bad")
for r in res:
    print Kott().get(r)

print ("\nFinding Koder Sina...")
res = Kott().find(name="Sina", tag="Koder")
for r in res:
    print Kott().get(r)

print ("\nFinding Coder Sina...")
res = Kott().find(name="Sina", tag="Coder")
for r in res:
    print Kott().get(r)

print ("\nFinding Koders...")
res = Kott().find(tag="Koder")
for r in res:
    print Kott().get(r)
