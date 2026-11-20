researcher = input("Введите имя исследователя: ")
exp_name = input("Введите название эксперимента: ")
runs_str = input("Введите количество запусков: ")
duration_str = input("Введите длительность одного запуска (с): ")
real_str = input("Введите действительную часть: ")
imag_str = input("Введите мнимую часть: ")

runs = int(runs_str)
duration = float(duration_str)
real_part = float(real_str)
imag_part = float(imag_str)

total_sec = runs * duration
total_min = total_sec / 60
coeff = complex(real_part, imag_part)
mod_sq = real_part ** 2 + imag_part ** 2
has_runs = bool(runs)

print("\n" + "=" * 40)
print(f"ЭКСПЕРИМЕНТ: {exp_name}")
print(f"Исследователь: {researcher}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_sec:.2f} с ({total_min:.2f} мин)")
print(f"Коэффициент: {coeff}")
print(f"Квадрат модуля: {mod_sq:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("=" * 40)

print("\n[Диагностика типов]")
print(f"Исследователь: {type(researcher)}, Эксперимент: {type(exp_name)}, "
      f"Запуски: {type(runs)}, Время: {type(duration)}, "
      f"Re: {type(real_part)}, Im: {type(imag_part)}")