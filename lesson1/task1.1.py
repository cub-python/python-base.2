# ЗАДАНИЕ 1
# Человеко-ориентированное представление интервала времени
# Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
# 1) до минуты: <s> сек;
# 2) до часа: <m> мин <s> сек;
# 3) до суток: <h> час <m> мин <s> сек;
# 4) сутки или больше: <d> дн <h> час <m> мин <s> сек
# Например, если пользователь введет 4567 секунд, вывести:
# 1 час 16 мин 7 сек
'''1 день = 24 ч., 1 ч = 60 мин, 1 мин = 60 сек; 60 мин * 60 сек = 3600 сек * 24 часа = 86400 сек.
1) namber // 86400 = получаем колич дня(// целочисленное деление, цифру до десятичн часть(целая часть.)
2) number = number  % (24*3600) = получаем остаток,и переменная получает новое значение
3) number(остаток) // 3600 = получаем целую часть(часы)
4) number // 60 = получаем целую часть(минуты)
5) number ровно на секунды.
'''
namber = int(input('Введите размер интервала: '))
d = namber // (24 * 3600)
namber = namber % (24 * 3600)
h = namber // 3600
h %= 3600
m = namber // 60
m %= 3600
s = namber
print(d, 'дн.', h, 'час.', m, 'мин', s, 'сек.')
