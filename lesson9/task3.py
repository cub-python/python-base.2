# 3. Реализовать базовый класс Employee (сотрудник).
# определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
# создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str), income
# (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus};
# в классе Position реализовать методы получения полного имени сотрудника get_full_name() и дохода с учётом
# премии get_total_income() (wage + bonus);
# проверить работу примера на реальных данных: создать экземпляры классов Employee, Position, вывести на экран
# имя сотрудника, его должность и вознаграждение сотрудника, используя методы класса Position.