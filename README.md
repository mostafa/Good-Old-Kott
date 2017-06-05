# Kott - an abstract data store
Kott is an abstract data store, where you can store anything
and retrieve it easily. Our motto is `One Kott fits all!`.
The whole idea is around the concept of a key-value store, but
has been abstracted to a level that can accept any form, model or
data. This means literally everything. Kott is singleton, so there
exists only a single instance of it.

```py
>>> from kott import Kott
>>> id = Kott.set("my test data which is a string!")
>>> len(id)
32
>>> type(id)
<type 'str'>
>>> Kott.get(id)
'my test data which is a string!'
```

As you can see, there is almost no need for storing the keys or
saving them somewhere, because you can always find your data.
For example, you can store the instances of your classes in Kott
and later access them using their keys. The magic happens with
the concept and implementation of Kott plugins or KPlugs.
Everything beyond the concept of key-value store is written
as kplug. There are official (bundled) kplugs, such as KTag,
KTimerPool, KString, ... . Every kplug adds its own keywords
to the core of Kott. So, if you want to tag your data while
inserting it into Kott, you just use the keyword `tag` as follows.
KPlugs are also singleton, and they have priorities while running,
so, a kplug with a lower value is executed before a kplug with a
higher value. To demonstrate the power and flexibility of Kott,
have a look at the example below. Official kplugs are called and
loaded by their name as string, but custom kplugs (written by users)
should be passed as instance.

```py
>>> Kott.load_kplug("KTag")  # True if loaded, False otherwise
True
>>> Kott.set(123, tag="my_numbers")
>>> Kott.set(456, tag="my_numbers")
>>> Kott.set(789, tag="my_numbers")
>>> ids = Kott.find(tag="my_numbers")
>>> for id in ids:
...     Kott.get(id)
123
456
789
```

The find method looks for keywords in each kplug, and starts searching
one by one to find the matching value, then it returns their IDs.

A sample kplug, KSample, is provided as an example for kplug developers.

:copyright: (c) 2016 by Hossein Ghannad, Sina Hatefmatbue, Mostafa Moradian
:license: GPLv3, see LICENSE for more details.