import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy
import math
import colorama

INERTIALESS_UNIT_NAME = 'Безынерционное звено'
APERIODIC_UNIT_NAME = 'Апериодическое звено'

def choice():
    need_new_choice = True
    while need_new_choice:
        print(colorama.Style.RESET_ALL)
        user_input = input('Введите номер команды: \n'
                           '1 - ' + INERTIALESS_UNIT_NAME + ';\n'
                           '2 - ' + APERIODIC_UNIT_NAME + '.\n')
        if user_input.isdigit():
            need_new_choice = False
            user_input = int(user_input)
            if user_input == 1:
                name = INERTIALESS_UNIT_NAME
            elif user_input == 2:
                name = APERIODIC_UNIT_NAME
            else:
                need_new_choice = True
                print(colorama.Fore.RED + '\nНедопустимое значение!')
        else:
            print(colorama.Fore.RED + '\nПожалуйста, введите числовое значение!')
    return name

def get_unit(unit_name):
    need_new_choice = True
    while need_new_choice:
        print(colorama.Style.RESET_ALL)
        need_new_choice = False
        if unit_name == INERTIALESS_UNIT_NAME:
            k = input('Введите коэффициент передачи звена (k): ')
            if k.isdigit():
                k = int(k)
                if unit_name == INERTIALESS_UNIT_NAME:
                    unit = matlab.tf([k], [1])
                else:
                    print(colorama.Fore.YELLOW + '\nНе реализовано!')
            else:
                print(colorama.Fore.RED + '\nПожалуйста, введите числовое значение!')
                need_new_choice = True
        elif unit_name == APERIODIC_UNIT_NAME:
            k = input('Введите коэффициент передачи звена (k): ')
            t = input('Введите постаянная времени звена (T): ')
            if k.isdigit() and t.isdigit():
                k = int(k)
                t = int(t)
                if unit_name == APERIODIC_UNIT_NAME:
                    unit = matlab.tf([k], [t, 1])
                else:
                    print(colorama.Fore.YELLOW + '\nНе реализовано!')
            else:
                print(colorama.Fore.RED + '\nПожалуйста, введите числовое значение!')
                need_new_choice = True
        else:
            print(colorama.Fore.YELLOW + '\nНедопустимое звено!')
            need_new_choice = True
    return unit

def graph(num, title, y, x):
    pyplot.subplot(2, 1, num)
    pyplot.grid(True)
    if title == 'Переходная характеристика':
        pyplot.plot(x, y, 'red')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x, y, 'black')
    pyplot.title(title)
    pyplot.xlabel('Время, с')
    pyplot.ylabel('Амплитуда')

unit_name = choice()
unit = get_unit(unit_name)
print(unit)

time_line = []
for i in range(0, 10000):
    time_line.append(i/1000)

[y, x] = matlab.step(unit, time_line)
graph(1, 'Переходная характеристика', y, x)
[y, x] = matlab.impulse(unit, time_line)
graph(2, 'Импульсная характеристика', y, x)
pyplot.show()