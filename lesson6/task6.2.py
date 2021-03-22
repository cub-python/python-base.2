# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер
# которых превышает объем ОЗУ компьютера.

result = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        elements = line.split()
        ip = elements[0]
        result.setdefault(ip, 0)
        result[ip] += 1
max_ipi = None
max_count = 0
for ip, ont in result.items():
    if ont > max_count:
        max_ip = ip
        max_count = ont

print('spammer', max_ip, max_count)
