# 1. Создать класс TrafficLight (светофор).
# определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
# после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью: красный (3 сек),
# жёлтый (1 сек), зелёный (3 сек);
# переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
# проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора с интервалом 0.5
# секунды, используя метод get_current_signal().