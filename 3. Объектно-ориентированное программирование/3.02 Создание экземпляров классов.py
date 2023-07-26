class Person:
    """Создаём человека"""

    def __init__(self, name, age, height):
        """Инициализируем аттрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описание человека"""
        description = self.name + ", ему " + str(self.age) + " лет, его рост " + str(
            self.height) + " см, его вес " + str(self.weight) + " кг"
        print("Нового человека зовут : " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес нашего человека : " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg



man = Person("Алекс", 30, 176)
# man.description_person()
# man.weight = 110
man.update_weight(120)
man.get_weight()


