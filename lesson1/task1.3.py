# ЗАДАНИЕ 3
# Сумма чисел из списка *
# Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (куб X - третья степень числа X):
#
# 1) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
#
# 2) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
# сумма цифр которых делится нацело на 7.
#
# 3) Написать алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков
# a
my_list = [3, 4, 5, 6, 7, 8]
print(sum(my_list))

# b
list_od = [i ** 3 for i in range(1, 1001, 2)]
print(list_od)
