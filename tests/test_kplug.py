from kott import Kott
from kott.kplugbase import KPlugBase


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
        print("I'm kissing " + str(value))
        return True

# @kSingleton
# class KTeacher(KPlugBase):
#     _data_type_ = Teacher
#
#     def on_set(self, key, value, **kwargs):
#         pass


def test_kplug():
    """
    You can either pass kplug class name (as String) or if it is a custom kplug,
    you can pass the instance of it like this:
    Kott.load_kplug(KSample())

    The below code loads the KSample kplug using its class name:
    Kott.load_kplug("KTag")

    The below code loads the KSample kplug using its instance:
    Kott.load_kplug(KStudent())
    """
    assert Kott.load_kplug(KStudent())
    assert Kott.load_kplug("KTag")
    assert Kott.set("Hello Kotto!")
    assert Kott.set("Wuzzup Kotto?")
    assert Kott.set("Bad Kotto!!!", tag="bad")


def test_ktag():
    s1 = Student("Sina", "G-")
    s2 = Student("Mostafa", "0+")
    s3 = Student("Sami", "Z-")
    s4 = Student("Yalda", "B+")

    assert Kott.set(s1, tag="Koder")
    assert Kott.set(s2, tag="Koder")
    assert Kott.set(s3, tag="Koder")
    assert Kott.set(s4, tag="Coder")


def test_find_with_attributes():
    print("\nFinding the bad...")
    res = Kott.find(tag="bad")
    for r in res:
        print(Kott.get(r))
        assert Kott.get(r)

    print("\nFinding all student whose names are Sina and was tagged as Koder...")
    res = Kott.find(name="Sina", tag="Koder")
    for r in res:
        print(Kott.get(r))
        assert Kott.get(r)

    print("\nFinding all students whose names are Sina and was tagged as Coder...")
    res = Kott.find(name="Sina", tag="Coder")
    for r in res:
        print(Kott.get(r))
        assert Kott.get(r)

    print("\nFinding all students tagged as Koder...")
    res = Kott.find(tag="Koder")
    for r in res:
        print(Kott.get(r))
        assert Kott.get(r)


def test_do_with_tagged_item():
    """
    Runs kiss on everything tagged as Coder 
    """
    print("\nDoing all Coders...")
    assert Kott.do("kiss", tag="Coder")
