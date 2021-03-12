# Задание 2. Курс Валюты
# Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
# Код валюты может быть в произвольном регистре.
# Функция должна возвращать результат числового типа, например float.
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
# http://www.cbr.ru/scripts/XML_daily.asp.
# Выведите на экран курсы для доллара и евро, используя написанную функцию.
# Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.


import requests


def get_currency_rate(currency):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if resp.status_code != 200:  # код ответа 200 это значит,можно получить полную инфо,если не 200 значить проблема.
        print('Данные с сайта ЦБ РФ не доступны')
        exit()
    content = resp.content.decode('windows-1251')  # кодировка не utf -8. получили  набор байта переоб к строке "decode

    parts = content.split('</Value><Value')  # найти нужн строку где наша валюта и раз
    currency_code = '<CharCode>' + currency.upper() + '</CharCode>'  # создаем переменную
    for part in parts:
        if currency_code in part:
            break
    else:
        return None  # по умолчанию

    currency_rate = float(part.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))  # делим на 2 части(по инд)
    # заменим,запятую на.точку,переобр к числу

    return currency_rate

for currency in ['USD', 'eur', 'CAD']:
    print(currency, get_currency_rate(currency))




