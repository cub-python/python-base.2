# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
# этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
# конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os    # импорт модуль ос

path = r'C:\Users\Admin\PycharmProjects\python-base.2\lesson7' #путь к папке
projectname = 'my_project'  # название проекта и ниже список папок. \ флеш переход на нов строку
folder = \
    ['settings',
     'mainapp',
     'adminapp',
     'authapp']

def createFolder(path):              # функция принимает новый путь
    if not os.path.exists(path):      # оператор if еси путь не сущ создаем папку
        os.mkdir(path)

fullPath = os.path.join(path, 'my_project')   # внутри модуля ос есть модуль path уоторого есть метод join для соедин путей
createFolder(fullPath)

for f in folder:
    folder = os.path.join(fullPath, f)
    createFolder(folder)
