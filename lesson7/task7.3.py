# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project1
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
# решена, например, во фреймворке django.


import os  # импорт модуль ос,создаём папку 'my_project1'

path = r'C:\Users\Admin\PycharmProjects\python-base.2\lesson7'
projectname = 'my_project1'
folder = \
    ['mainapp',
     'authapp']


def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)


fullPath = os.path.join(path, 'my_project1')
createFolder(fullPath)

for f in folder:
    folder = os.path.join(fullPath, f)
    createFolder(folder)

os.makedirs('mainapp/base.html/index.html')
os.makedirs('authapp/base.html/index.html')
