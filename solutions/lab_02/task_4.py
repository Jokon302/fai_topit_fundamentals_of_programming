import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)
print("GC включен?:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Счетчики поколений:", gc.get_count())

print("id списков:", id(first), id(second))

del first
del second

collected = gc.collect()
print("gc.collect() собрал объектов:", collected)

gc.disable()
print("\nGC отключен?:", not gc.isenabled())

cycles = []
for _ in range(5):
    a = []
    b = [a]
    a.append(b)
    cycles.append(a)

del cycles
print("Счетчики до ручной сборки:", gc.get_count())
manual_collected = gc.collect()
print("Собрано вручную при отключенном GC:", manual_collected)

gc.enable()
print("GC снова включен?:", gc.isenabled())

before_graph = gc.collect()
print("\nДо создания графа собрано:", before_graph)

node_a = {"name": "A", "links": []}
node_b = {"name": "B", "links": []}
node_c = {"name": "C", "links": []}
node_d = {"name": "D", "links": []}

node_a["links"].append(node_b)
node_b["links"].append(node_c)
node_c["links"].append(node_a)
node_d["links"].append("данные")

print("Связи графа: A -> B -> C -> A; D независим")
del node_a
del node_b
del node_c

after_graph = gc.collect()
print("После удаления графа собрано:", after_graph)
print(f"Сравнение сборки: до создания графа {before_graph}, после удаления графа {after_graph}")

assert node_d["name"] == "D"
print("Узел D остался жив и доступен:", node_d)
