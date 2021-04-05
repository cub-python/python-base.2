# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя
# пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?


# re.compile(pattern, flags). который выполняет компиляцию регулярного выражения и
# возвращает его в виде экземпляра класса Pattern.

import re

re_email = re.compile('^([\w, \d, .]+)@((([\w, \d, .]+)\.)+[\w]+)$')  # передаем параметры компиляции


def email_parse(email):                  # парсируем создав функ email_parse
    match = re_email.match(email)       #  match используется для поиска в начале строки подстроки, которая соответствует шаблону

    if match:
        return {'username': match.group(1), 'domain': match.group(2)} #  возвращает  если подстрока найдена

    else:
        raise ValueError('неккоректный почтовый адрес')   #  возвращает ValueError, если подстрока  не найдена


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
