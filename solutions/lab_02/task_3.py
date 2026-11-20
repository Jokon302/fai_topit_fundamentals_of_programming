import sys
import weakref

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

registry = weakref.WeakValueDictionary()
rec1 = Record()
rec2 = Record()
temp = Record()

registry["first"] = rec1
registry["second"] = rec2
registry["temp"] = temp

print("Реестр в начале:", list(registry.keys()))

del temp
print("После del temp:", list(registry.keys()))

del rec1
print("После del rec1:", list(registry.keys()))
