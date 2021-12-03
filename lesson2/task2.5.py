# Задание 5
# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп.
# Например:
# 57 руб 08 коп, 46 руб 51 коп, 97 руб 00 коп, ...
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек
# или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
prices = [
    36.41, 17.23, 98.54, 63.11, 78.77, 54.47,
    91 / 23, 35.75, 62.34, 80.11, 27.39, 33.74
]
print(id(prices))  # напечатать id прайс
prices.sort()  # сортируем
print(id(prices))  # вернём обратно
for price in prices:
    rubles = int(price)
    renny = int(price + 100) % 100
    print(f'{rubles} руб {renny:02} коп')
print('xxxxxxxxxxxxxxxx')
new_price_list = sorted(prices, reverse=True)  # создали нов список цен,повт перв опер с прайс.
print(id(new_price_list))
for price in new_price_list:
    rubles = int(price)
    renny = int(price + 100) % 100
    print(f'{rubles} руб {renny:02} коп')
print('xxxxxxxxxxx')
# по возраст выбрать самые дорогие 5 цен.
for price in new_price_list[:5]:
    rubles = int(price)
    renny = int(price + 100) % 100
    print(f'{rubles} руб {renny:02} коп')
