import math
x = 17
y = 5
print("x + y  =", x + y, type(x + y))
print("x - y  =", x - y, type(x - y))
print("x * y  =", x * y, type(x * y))
print("x / y  =", x / y, type(x / y))   
print("x // y =", x // y, type(x // y))   
print("x % y  =", x % y, type(x % y))     
print("x ** y =", x ** y, type(x ** y))  
print("-" * 40)

big_number = 2 ** 1000
print("2 ** 1000 =", big_number)
print("Тип 2 ** 1000:", type(big_number))

print("-" * 40)

result = 0.1 + 0.2
print("result:", result)
print("result == 0.3:", result == 0.3)
print("result - 0.3:", result - 0.3)
print("math.isclose(result, 0.3):", math.isclose(result, 0.3))

print("-" * 40)

print('int("42"):', int("42"), type(int("42")))
print('float("3.14"):', float("3.14"), type(float("3.14")))
print('str(2026):', str(2026), type(str(2026)))
print('bool(0):', bool(0), type(bool(0)))
print('bool(-1):', bool(-1), type(bool(-1)))
print('bool(""):', bool(""), type(bool("")))
print('bool("False"):', bool("False"), type(bool("False")))

comp = complex(2, -3)
print("complex(2, -3):", comp, type(comp))
print("Действительная часть:", comp.real)
print("Мнимая часть:", comp.imag)

print(13.7 // 6)