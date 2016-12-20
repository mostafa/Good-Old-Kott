from kott import Kott
from kott.kplugbase import KPlugBase
from kott.kplugs import ksample
from kott.kplugs import ktags


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
# return "Teacher: " + self.name + ", Students: " +
# len(self.teacher_students)


class KStudent(KPlugBase):
    _data_type_ = Student
    _keywords_ = ["name"]

    def on_find_visit(self, key, value, **kwargs):
        if value.name == kwargs["name"]:
            return True
        return False

    def kplug_do_kiss(self, key, value, **kwargs):
        print "I'm kissing " + str(value)

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
s4 = Student("Yalda", "B+")

Kott().set(s1, tag="Koder")
Kott().set(s2, tag="Koder")
Kott().set(s3, tag="Koder")
Kott().set(s4, tag="Coder")

print ("\nFinding the bad...")
res = Kott().find(tag="bad")
for r in res:
    print Kott().get(r)

print ("\nFinding all student whose names are Sina and was tagged as Koder...")
res = Kott().find(name="Sina", tag="Koder")
for r in res:
    print Kott().get(r)

print ("\nFinding all students whose names are Sina and was tagged as Coder...")
res = Kott().find(name="Sina", tag="Coder")
for r in res:
    print Kott().get(r)

print ("\nFinding all students tagged as Koder...")
res = Kott().find(tag="Koder")
for r in res:
    print Kott().get(r)

print ("\nDoing all Coders...")
Kott().do("kiss", tag="Coder")
