# """
# Создаём переменную fw и присваем ей значение open (открыть)
# в которой мы указываем, что хотим создать "doc/file.txt"
# указываем мод 'a', позволяющий записывать в файл инфо
#  и помещать созданную запись в конец нашего списка
# """
# fw = open("doc/file.txt", 'a')
# """
# записываем переменную и применяем к ней функцию write
# в которую помещаем "Hello, world!", позже он будет записан
# в наш file.txt
# """
# fw.write("Hello world\n") # \n - переносит на новую строку
# # закрываем наш файл
# fw.close()

# Второй вариант с использованием input
# var = input("Напиши что-нибудь : ")
# fw = open("doc/file.txt", 'a')
# fw.write(var)
# fw.close()

# a - запись новых данных, в файл и помещение новых данных в конец файла
# w - запись новых данных, но с удалением старых данных
# r - чтение данных содержимого нашего файла

# fw = open("doc/file2.txt", 'w')
# fw.write("privet!!!")
# fw.close()

fr = open("doc/file.txt", 'r')
text = fr.read()
fr.close()
print(text)

