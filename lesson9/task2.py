# 2. Реализовать класс Road (дорога).
# определить защищенные атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# определить внутри класса приватную константу масса квадратного метра асфальта толщиной 1 см.
# определить метод расчёта массы асфальта get_asphalt_mass(height), необходимого для покрытия
# всей дороги толщиной height см;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги
# асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 8     # автомобильная дорога: для дорог с интенсивным движением, каждый пласт должен быть не меньше 4 см, всего может быть от 2 до 4 слоев; 8 см.

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height/1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} массы асфальта')


r = Road(5000, 20)
r.asphalt_mass()