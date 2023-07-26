# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)
#
#
# num_1 = 30
# num_2 = 40
# result = num_1 + num_2
# print(result)

# def - так обозначается функция, а summ - это её название
# def summ(num_1, num_2):
#     result = num_1 + num_2
#     print(result)
#
#
# # для запуска функции нужно написать с новой строчки summ(), где в скобках укажем числа для суммирования
# summ(10, 20)
# # можно продублировать ещё раз эти строчки
# summ(30, 20)

# def summ(num_1, num_2):
#     result = num_1 + num_2
#     print(result)
#
# # num_1 это будет "Hello", а num_2 это будет "world"
# # Если поменять местами слова, то поменяется порядок переменных
# summ("Hello", "world")
# # если поменять местами переменные со словами, то будет всё по порядку
# summ(num_2="world", num_1="Hello")

# # функция приветствия
# def hi(name="Alex"):
#     print("Hello " + name)
#
# hi()


# # функция приветствия 2
# name = "Alex"
# def hi(name):
#     print("Hello " + name)
#
# hi(name)

# # функция приветствия c age
# name = "Алекс"
# def hi(name, age):
#     print("Меня зовут " + name + " мне " + age + " лет")
#
# hi(name, "30")

# # функция приветствия c age (вариант 2)
# def hi(name, age):
#     print("Меня зовут " + name + " мне " + age + " лет")
#
# hi("Алекс", "30")

# # функция приветствия c input
# name = input("Введите ваше имя: ")
# age = int(input("Введите ваш возраст: "))
# def hi(name, age):
#     print("Меня зовут " + name + " мне " + str(age) + " лет")
#
# hi(name, age)

# функция приветствия c return
name = "Alex"
age = "33"
def hi(name, age):
    result = name + " " + age
    # return возвращает результат
    return result

h = hi(name, age)
print(h)
