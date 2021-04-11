# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу
# на данных,вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

def div():
        try:
            user_num_1 = int(input('Ведите числитель:  '))
            user_num_2 = int(input('Ведите делитель:  '))
            if user_num_2 == 0 or user_num_2 > user_num_1:
                raise OwnError('Ошибочка вышла, так делить нельзя!')
            # else:
            #     user_num_1 < user_num_2
            #     raise OwnError('Ошибка,делитель больше чем числитель') хотел ещё раз или включать никак
            else:
                res = user_num_1 / user_num_2
                return res

        except ValueError:
            return 'Вы ввели не число'

        except OwnError as err:
            return err

print(div())

