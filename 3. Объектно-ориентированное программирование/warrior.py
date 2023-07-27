from base_person import Person

class Warrior(Person):
    """Создание класса воина"""
    def __init__(self, name, age, height):
        """Инициализируем аттрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд ярости равен : " + str(self.rage))

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ", ему " + str(self.age) + " лет, его заряд ярости " + str(
            self.rage)
        # print("Нового человека зовут : " + description)
        return description


warrior = Warrior("Конон", 35, 200)
print("Нового человека зовут : " + warrior.description_person())