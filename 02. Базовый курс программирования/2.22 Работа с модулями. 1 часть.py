# импортируем библиотеки
import hello
import math
import random
# hello.some_1()
# print(math.pi)
# в переменной указываем библиотеку и выбирваем функцию
r = random.randrange(0, 10)
# каждый раз будет выводиться рандомное число на экран
user = 'User '
user_random = user + str(r)
print(user_random)