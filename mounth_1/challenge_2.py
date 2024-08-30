"""
+---------------------------------------------------+
|						TEST						|
+---------------------------------------------------+
"""

def calculator(num_1:float, action:str, num_2:float) -> float:
    """
    Принимает число 1, арифметический оператор, число 2
    Возвращает результат арифметической операции
    """
    try:
        # return eval(num_1 + action + num_2)   # Плохой вариант, но иногда может пригодиться (выполняет строку как функию)
        num_1, action, num_2 = float(num_1), action.strip(), float(num_2)
        match action:
            case '+':
                return num_1 + num_2
            case '-':
                return num_1 - num_2
            case '*':
                return num_1 * num_2
            case '/':
                return num_1 / num_2
            case '**':
                return num_1 ** num_2
            case '//':
                return num_1 // num_2
            case '%':
                return num_1 % num_2
            case _:
                print('Такой арифметический оператор не существует')
    except ValueError:
        print('Переменные должны быть числами!')
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
    except:
        print('Неизвестная ошибка!')

print(calculator(6.2, ' +'))
