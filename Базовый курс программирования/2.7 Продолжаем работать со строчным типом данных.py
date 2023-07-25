# str_1 = "Hello"
# str_2 = "WORLD"
# # print(str_1)
# # #dir показывает список всех действий и функций, которые применимы к типу string
# # print(dir(str_1))
# # upper - функция, которая переводит все наши значения в заглавные буквы
# print(str_1.upper())
# # upper - функция, которая переводит первое значение с заглавной буквы
# print(str_1.title())
# # lower - функция, которая переводит все наши значения в строчные буквы
# print(str_1.lower())

# # Создаём переменную name и присваиваем значение "Ivan"
# name = "Ivan"
# name = "Alex" #читаться будет Alex, т.к. читается снизу вверх
# # Создаём переменную a и присваиваем значение "hello {}"
# a = "Hello {}"
# # Создаём переменную result и присваиваем значение a.format, где в скобках помещаем (name)
# result = a.format(name)
# # Выводим на экран result
# print(result)

# # Способ номер 2
# first_name = "Ivan"
# last_name = "Ivanov"
# a = "{} {}"
# result = a.format(first_name, last_name)
# print("Меня зовут: " + result)

# Способ номер 3 f'string
first_name = "Ivan"
last_name = "Ivanov"
result = f'{first_name} {last_name}'
print("Меня зовут: " + result)


