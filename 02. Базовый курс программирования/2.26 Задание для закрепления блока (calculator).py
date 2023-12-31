"""
Напишите проект "Калькулятор".

Инструкции к заданию:

Напишите скрипт "калькулятор",
который будет принимать от пользователя на вход:

1-е число

арифметический знак, один из: +, -, *, /

2-е число

производить сложение, вычитание, умножение или деление,
в зависимости от введенного знака

А так же предусмотрите проверку на то, что на ноль делить нельзя.
И другие виды некорректно введенных данных.

Данное задание Вам необходимо выполнить самостоятельно
и стараться не пользоваться сторонними источниками

Ответ в виде текста, прошу приложить в Решения или прислать на почту aleksandr_stepik@mail.ru


ДРУЗЬЯ, ЕЩЕ РАЗ: КАЛЬКУЛЯТОР ДОЛЖЕН УМЕТЬ СКЛАДЫВАТЬ, ВЫЧИТАТЬ, УМНОЖАТЬ, ДЕЛИТЬ.
НЕ ТОЛЬКО ДЕЛИТЬ!!! ПРИ ЧЕМ ДЕЙСТВИЕ ВЫПОЛНЯЕТСЯ ИСХОДЯ ИЗ ТОГО КАКОЙ ЗНАК ВВЕЛ ПОЛЬЗОВАТЕЛЬ!

"""
# Calculator
num_1 = float(input('Введите первое число: '))
symbol = input('Выберите один из знаков: +, -, *, /: ')
num_2 = float(input('Введите второе число: '))
if symbol == '+':
    result = int(num_1 + num_2)
    print(f'Результат равен: {result}')
elif symbol == '-':
    result = int(num_1 - num_2)
    print(f'Результат равен: {result}')
elif symbol == '*':
    result = int(num_1 * num_2)
    print(f'Результат равен: {result}')
elif symbol == '/':
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        result = 0
        print('На ноль делить нельзя!')
    print(f'Результат равен: {result}')
else:
    print('Такой знак использовать нельзя!')
