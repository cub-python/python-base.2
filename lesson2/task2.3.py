# Задание 3
# вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.

a_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
a_list_index = 0
while a_list_index < len(a_list):
    element = a_list[a_list_index]
    if element.isdigit():
        a_list[a_list_index] = f'{int(element):02}'
        a_list.insert(a_list_index, '"')
        a_list.insert(a_list_index + 2, '"')
        a_list_index += 3
    elif (element[0] == '+' or element[0] == '-') and element[1:].isdigit():
        sign = element[0]
        a_list[a_list_index] = f'{int(element[1:]):02}'
        a_list.insert(a_list_index, '"')
        a_list.insert(a_list_index + 2, '"')
        a_list_index += 3
    else:
        a_list_index += 1
result = ' '.join(a_list)
print(result)
