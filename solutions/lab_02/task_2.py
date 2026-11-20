import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

print("Начальное состояние:")
print("original:", original)
print("alias:   ", alias)
print("shallow: ", shallow)
print("deep:    ", deep)
print("id внешних:", id(original), id(alias), id(shallow), id(deep))
print("id [0]:    ", id(original[0]), id(alias[0]), id(shallow[0]), id(deep[0]))
print("id оценки: ", id(original[0][1]), id(alias[0][1]), id(shallow[0][1]), id(deep[0]))

original.append(["Databases", 5])
print("\nПосле append:")
print("original:", original)
print("alias:   ", alias)
print("shallow: ", shallow)
print("deep:    ", deep)
print("id внешних:", id(original), id(alias), id(shallow), id(deep))
print("id [0]:    ", id(original[0]), id(alias[0]), id(shallow[0]), id(deep[0]))
print("id оценки: ", id(original[0][1]), id(alias[0][1]), id(shallow[0][1]), id(deep[0]))

original[0][1] = 3
print("\nПосле изменения оценки:")
print("original:", original)
print("alias:   ", alias)
print("shallow: ", shallow)
print("deep:    ", deep)
print("id внешних:", id(original), id(alias), id(shallow), id(deep))
print("id [0]:    ", id(original[0]), id(alias[0]), id(shallow[0]), id(deep[0]))
print("id оценки: ", id(original[0][1]), id(alias[0][1]), id(shallow[0][1]), id(deep[0]))

print("\nМатрицы:")
wrong_matrix = [[0] * 3] * 3
print("wrong_matrix до:", wrong_matrix)
wrong_matrix[0][0] = 1
print("wrong_matrix после:", wrong_matrix)
print("id строк wrong:", [id(row) for row in wrong_matrix])

correct_matrix = [[0] * 3 for _ in range(3)]
print("correct_matrix до:", correct_matrix)
correct_matrix[0][0] = 1
print("correct_matrix после:", correct_matrix)
print("id строк correct:", [id(row) for row in correct_matrix])
