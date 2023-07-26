# Цикл For проходит по списку элементов - идеально подходит для списков

# Создаём переменную students, в которую вносим список студентов
# students = ["Alex", "Ivan", "Olga", "Semen", "Igor", "Svetlana"]

"""
Создаём цикл с переменной f,
которая будет обращаться к каждому элементу нашего списка по очереди
и указали из какого списка брать (из students).
Цикл for проходит по нашему списку и каждый элемент присваивает 
в качестве значения к переменной f и потом выводим на экран.
P.S.название переменной может быть любой, не обязательно f)
"""
# for f in students:
#     print(f)

# Вариант 2 с переменной var
# students = ["Alex", "Ivan", "Olga", "Semen", "Igor", "Svetlana"]
#
# for f in students:
#     # используем конкатенацию строк
#     var = "Инженер " + f
#     print(var)
#

# Вариант 3 с использованием if
# students = ["Alex", "Ivan", "Olga", "Semen", "Igor", "Svetlana"]
#
# for f in students:
#     if f == "Olga":
#         var = "Инженер " + f
#         print(var)

# Вариант 4 с использованием списка
# students = ["Alex", "Ivan", "Olga", "Semen", "Igor", "Svetlana"]
#
# for f in students[:3]: # вывела 3 первых элемента из нашего списка
# # for f in students[3:]: # вывела 3 последних элемента из нашего списка
# # for f in students[1:4]: # вывела с 1 до 4 элемента из нашего списка
#     print(f)


# Вариант 4 с использованием len
students = ["Alex", "Denis", "Yan", "Semen", "Igor", "Svetlana"]

for f in students:
    # выведет количество символов в каждом элементе
    print(len(f))
