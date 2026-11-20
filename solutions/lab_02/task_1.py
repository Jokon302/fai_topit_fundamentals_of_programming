a = 10
b = a
print("До a += 1:")
print(a, b)
print(id(a), id(b))

a += 1
print("После a += 1:")
print(a, b)
print(id(a), id(b))

first = [10, 20]
second = first
print("\nДо append:")
print(first, second)
print(id(first), id(second))

second.append(30)
print("После second.append(30):")
print(first, second)
print(id(first), id(second))

second = [10, 20, 30]
print("\nСравнение после переназначения:")
print("first == second:", first == second)
print("first is second:", first is second)

second.append(40)
print("first:", first)
print("second:", second)

conf1 = {
    "name": "Проект 1",
    "members": ["Иван", "Маша"],
    "params": ["--debug", "--port=8000"]
}
conf2 = conf1
conf2["name"] = "Проект 2"
conf2["members"].append("Петя")
conf2["params"][0] = "--release"

print("\nПрисваивание conf2 = conf1 (до и после изменений):")
print("conf1:", conf1)
print("conf2:", conf2)

conf1 = {
    "name": "Проект 1",
    "members": ["Иван", "Маша"],
    "params": ["--debug", "--port=8000"]
}
conf2 = {
    "name": "Проект 2",
    "members": conf1["members"][:] + ["Петя"],
    "params": ["--release", conf1["params"][1]]
}

print("\nСоздание независимой конфигурации (до и после изменений):")
print("conf1:", conf1)
print("conf2:", conf2)

print("\nИтог связей объектов:")
print("Словари:   ", "общие" if conf1 is conf2 else "независимые")
print("members:   ", "общие" if conf1["members"] is conf2["members"] else "независимые")
print("params:    ", "общие" if conf1["params"] is conf2["params"] else "независимые")

assert conf1["name"] != conf2["name"]
assert conf1["members"] != conf2["members"]
assert conf1["params"] != conf2["params"]
assert conf1["members"] is not conf2["members"]
assert conf1["params"] is not conf2["params"]
print("Проверки assert пройдены")
