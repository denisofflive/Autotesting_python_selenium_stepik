"""Создание класса"""
class Car():

    def __init__(self, model, made_in_year, engine_volume, price, mileage):
        """Инициализация атрибутов класса Car"""
        self.model = model
        self.made_in_year = made_in_year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels_num = 4
        # print('Новая машина создана')


    def get_description(self):
        """Получение информации о созданной машине"""
        description = 'Модель ' + str(self.model) + ' выпущена в ' + str(self.made_in_year) + ' году.'\
        + ' Объём двигателя - ' + str(self.engine_volume) + ' л,' + ' пробег - ' + str(self.mileage) + ' км/г, '\
        + 'количество колёс - ' + str(self.wheels_num) + ' шт. ' + 'Cтоимость равна ' + str(self.price) + '$.'
        return description


class Truck(Car):
    """Cоздание класса-наследника Грузовик"""

    def __init__(self, model, made_in_year, engine_volume, price, mileage):
        """Инициализация атрибутов класса родителя"""
        super().__init__(model, made_in_year, engine_volume, price, mileage)

    def update_wheels_num(self):
        """Изменение количества колёс у грузовика"""
        self.wheels_num = 8