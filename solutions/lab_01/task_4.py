student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10
print("Первый символ:", student[0])
print("Последний символ:", student[-1])
first_name = student[:4]
last_name = student[5:]
print("Имя:", first_name)
print("Фамилия:", last_name)
print("Верхний регистр:", student.upper())
print("Нижний регистр:", student.lower())

initials = f"{student[0]}.{student[5]}."
print("Инициалы:", initials)
print("Курс наоборот:", course[::-1])

percentage = (completed / total) * 100
res_percent = "%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percentage)

res_format = "{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percentage)

res_fstring = f"{student} — {course}: {completed}/{total} ({percentage:.1f}%)"

print("Результат (%):", res_percent)
print("Результат (.format):", res_format)
print("Результат (f-строка):", res_fstring)
symbol = "Я"
code_point = ord(symbol)
restored_symbol = chr(code_point)
encoded_bytes = symbol.encode("utf-8")

print(f"Символ: {symbol}")
print(f"Кодовая позиция (ord): {code_point}")
print(f"Восстановленный символ (chr): {restored_symbol}")
print(f"Байты (UTF-8): {encoded_bytes}")
print(f"Длина строки: {len(symbol)}, Длина байтов UTF-8: {len(encoded_bytes)}")
# student[0] = "О"  # TypeError: 'str' object does not support item assignment