# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

outputfile = '../new_line.txt'             # наз конечн файла
new_line = '[27/May/2015:05:05:44 +0000]'  # поиск по этим данным

f = open('nginx_logs.txt', 'r', encoding='utf-8')              # открываем файл для читение в коде 'utf-8'
f2 = open(outputfile, 'w', encoding='utf-8')                   # редактируем кон файл  в коде 'utf-8'

for line in f:                                                      # запускаем цикл в файле по строчно
    if new_line in line:
        line = line.replace('-', '').replace('"', '').replace('  ', '')     # удаляем -(дефисы),"(кавычки) и пробелы
        item = line.split(' ')                                 # делим строку
        str = (item[0], item[3], item[4])                      # выбираем нужн элементы
        print(str)                                            # печатаем
f.close()
f2.close()



    f2.write('found line' + line)


