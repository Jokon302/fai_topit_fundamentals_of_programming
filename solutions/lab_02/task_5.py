import sys
import tracemalloc

print("Размеры объектов (sys.getsizeof):")
print("Пустой список []:     ", sys.getsizeof([]), "байт")
print("Список из 10 чисел:   ", sys.getsizeof(list(range(10))), "байт")
print("Кортеж из 10 чисел:   ", sys.getsizeof(tuple(range(10))), "байт")
print("Строка из 10 символов:", sys.getsizeof("0123456789"), "байт")
print("Число 42:             ", sys.getsizeof(42), "байт")
print("Объект None:          ", sys.getsizeof(None), "байт")

print("\nРост списка (100 append):")
lst = []
prev_size = sys.getsizeof(lst)
print(f"Старт: длина {len(lst)}, размер {prev_size} байт")

for i in range(1, 101):
    lst.append(i)
    cur_size = sys.getsizeof(lst)
    if cur_size != prev_size:
        print(f"Шаг {len(lst)}: размер стал {cur_size} байт (+{cur_size - prev_size})")
        prev_size = cur_size

print("\ntracemalloc (list vs range):")

tracemalloc.start()
numbers_list = list(range(100_000))
cur_list, peak_list = tracemalloc.get_traced_memory()
tracemalloc.stop()
del numbers_list

tracemalloc.start()
numbers_range = range(100_000)
cur_range, peak_range = tracemalloc.get_traced_memory()
tracemalloc.stop()
del numbers_range

cur_list_kb = cur_list / 1024
peak_list_kb = peak_list / 1024
cur_range_kb = cur_range / 1024
peak_range_kb = peak_range / 1024

print(f"list(range(100_000)): Текущая {cur_list_kb:.2f} KB, Пиковая {peak_list_kb:.2f} KB")
print(f"range(100_000):       Текущая {cur_range_kb:.2f} KB, Пиковая {peak_range_kb:.2f} KB")

scenarios = [
    {
        "name": "list(range(100_000))",
        "count": 100_000,
        "size": sys.getsizeof(list(range(100_000))),
        "cur_kb": cur_list_kb,
        "peak_kb": peak_list_kb,
    },
    {
        "name": "range(100_000)",
        "count": 100_000,
        "size": sys.getsizeof(range(100_000)),
        "cur_kb": cur_range_kb,
        "peak_kb": peak_range_kb,
    },
]

print("\nИтоговый отчет:")
print(f"{'Сценарий':<22} | {'Элементов':<10} | {'getsizeof':<10} | {'Текущая':<10} | {'Пиковая':<10}")
print("-" * 72)
for s in scenarios:
    print(f"{s['name']:<22} | {s['count']:<10} | {s['size']:<8} B | {s['cur_kb']:<7.2f} KB | {s['peak_kb']:<7.2f} KB")

ratio = scenarios[0]["size"] / scenarios[1]["size"]
print(f"\nПо getsizeof список больше в {ratio:.1f} раз")
print(f"По пиковой памяти список ~{peak_list_kb:.0f} KB, а range ~{peak_range_kb:.2f} KB")
