# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# src.sort()
# print(src)
#############
for e in range(1, len(src)):
    if src[e] > src[e - 1]:
        print(src[e], end = " ")