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


object_key = ""
result = []


def test_kott():
    global object_key
    print("---------- Testing Kott ----------")
    object_key = Kott.set("Hello Kott!")
    object_value = Kott.get(object_key)
    print("Key: " + str(object_key) + ", Value: " + str(object_value))
    assert object_value == "Hello Kott!"


def test_load_kplug():
    # Load kplugs
    assert Kott.load_kplug("KTag")
    assert Kott.load_kplug("KSample")
    assert Kott.load_kplug("KString")


def test_ktag():
    # Load sample data
    assert Kott.set("Tagged value no.1", tag="Test Tag")
    assert Kott.set("Tagged value no.2", tag="Test Tag")
    assert Kott.set("Tagged value no.3", tag="Test Tag")


def test_custom_object():
    assert Kott.set(Student("Sina", "F-"))
    assert Kott.set(Student("Mostafa", "F+"))
    assert Kott.set(Student("Sami", "Z-"))


def test_internal_data_types():
    assert Kott.set(100)
    assert Kott.set(1000)
    assert Kott.set(10000)


def test_ksample():
    global object_key
    print("---------- Testing Sample KPlug ----------")

    object_value = Kott.get(object_key, sample_arg="A Sample Argument for GET")
    print("Key: " + str(object_key) + ", Value: " + str(object_value))
    assert object_value

    object_key = Kott.set(
        "Sample Data", sample_arg="A Sample Argument for SET")
    assert object_key
    object_value = Kott.get(
        object_key, sample_arg="A Sample Argument for GET again!")
    assert object_value
    print("Key: " + str(object_key) + ", Value: " + str(object_value))

    Kott.delete(object_key)


def test_ktag_on_find():
    global result
    print("---------- Testing KTags ----------")
    result = Kott.find(tag="Test Tag")
    for r in result:
        print(Kott.get(r))
        assert Kott.get(r)


def test_kstring():
    global result
    print("---------- Testing KStrings ----------")

    print("--- Test str_equal")
    result = Kott.find(str_equal="Tagged value no.3")
    for r in result:
        print(Kott.get(r))
        assert Kott.get(r)

    print("--- Test str_has")
    result = Kott.find(str_has="Grade")
    for r in result:
        print(Kott.get(r))
        assert Kott.get(r)

    print("--- Test str_regex 1")
    result = Kott.find(str_regex=".*F.*")
    for r in result:
        print(Kott.get(r))
        assert Kott.get(r)

    print("--- Test str_regex 2")
    result = Kott.find(str_regex=".*gg\w.*")
    for r in result:
        print(Kott.get(r))
        assert Kott.get(r)

    print("--- Test str_regex 3 (The Magical Sum)")
    result = Kott.find(str_regex="^\d+")
    assert result
    print(sum([Kott.get(i) for i in result]))
    assert sum([Kott.get(i) for i in result])


def test_update():
    global result
    print("--- Testing update")
    assert Kott.update(result[0], 99)
    print(sum([Kott.get(i) for i in result]))
    assert sum([Kott.get(i) for i in result])


def test_update_tag():
    global result
    print("--- Update data and set tag on them")
    result = Kott.find(str_regex="^\d+")
    for key in result:
        assert Kott.update(key, tag="numerals")

    print([Kott.get(key) for key in Kott.find(tag="numerals")])
    assert [Kott.get(key) for key in Kott.find(tag="numerals")]

    print("--- Update tag")
    for key in result:
        assert Kott.update(key, tag="Decimal")

    print([Kott.get(key) for key in Kott.find(tag="Decimal")])
    assert [Kott.get(key) for key in Kott.find(tag="Decimal")]


def test_cleanup():
    Kott.cleanup()
