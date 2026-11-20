import sys
import tracemalloc


def measure(name, count, create):
    tracemalloc.start()
    obj = create()
    cur, peak = tracemalloc.get_traced_memory()
    size = sys.getsizeof(obj)
    tracemalloc.stop()
    return {
        "name": name,
        "count": count,
        "size": size,
        "cur": cur,
        "peak": peak,
    }


# 1. Размеры отдельных объектов
sizes = [
    ("Пустой список []", 0, sys.getsizeof([])),
    ("Список из 10 чисел", 10, sys.getsizeof(list(range(10)))),
    ("Кортеж из 10 чисел", 10, sys.getsizeof(tuple(range(10)))),
    ("Строка из 10 символов", 10, sys.getsizeof("0123456789")),
    ("Число 42", 1, sys.getsizeof(42)),
    ("None", 0, sys.getsizeof(None)),
]

# 2. Рост списка: сохраняем только шаги, где размер изменился
lst = []
start_size = sys.getsizeof(lst)
growth = [(0, start_size, None)]
prev = start_size
for i in range(1, 101):
    lst.append(i)
    size = sys.getsizeof(lst)
    if size != prev:
        growth.append((len(lst), size, size - prev))
        prev = size
del lst

# 3. Сравнение list и range
scenarios = [
    measure("list(range(100_000))", 100_000, lambda: list(range(100_000))),
    measure("range(100_000)", 100_000, lambda: range(100_000)),
]

# Печать результатов
print("РАЗМЕРЫ ОБЪЕКТОВ")
print(f"{'Объект':<28}{'Элементов':>10}{'Размер, B':>11}")
for name, count, size in sizes:
    print(f"{name:<28}{count:>10}{size:>11}")

print("\nРОСТ СПИСКА")
print(f"{'Длина':>6}{'Размер, B':>11}{'Прирост':>10}")
for length, size, delta in growth:
    if delta is None:
        print(f"{length:>6}{size:>11}{'-':>10}")
    else:
        print(f"{length:>6}{size:>11}{'+' + str(delta):>10}")

print("\nLIST И RANGE")
print(f"{'Сценарий':<22}{'Элементов':>10}{'getsizeof':>11}{'Текущая, KB':>13}{'Пиковая, KB':>13}")
for row in scenarios:
    print(f"{row['name']:<22}{row['count']:>10}{row['size']:>11}{row['cur'] / 1024:>13.2f}{row['peak'] / 1024:>13.2f}")

list_row, range_row = scenarios
print(f"\nПо getsizeof: в {list_row['size'] / range_row['size']:.1f} раз больше")
if range_row["peak"]:
    print(f"По пиковой памяти: в {list_row['peak'] / range_row['peak']:.1f} раз больше")
else:
    print("По пиковой памяти: не определено (у range 0 KB)")
    print(f"range в tracemalloc не учтён, его размер по getsizeof — {range_row['size']} B")
