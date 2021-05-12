# 6-1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time

class TrafficLight:
    __color = {"красный": 7, "желтый": 2, "зеленый": 4}
    pause = 0

    def running(self):
        color_dict = self.__color
        for key, el in enumerate(color_dict):
            pause = color_dict.get(el)
            print(f"{el} горит {pause} секунды")
            time.sleep(pause)


TrafficLight().running()


# 6-2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_calculating_mass(self):
        return self._length * self._width * 25 * 5

asphalt_masses = Road(20, 5000).get_calculating_mass()
print(asphalt_masses)


# 6-3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

income = {"wage": 1000, "bonus": 10}

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


    def get_name(self):
        return self.name

    def get_income(self):
        return self._income

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        income_list = self.get_income()
        wage = income_list['wage']
        bonus = income_list['bonus']
        return wage * bonus


work = Position('Alexey', 'Kynin', 'engineer', income)

print(f"Сотрудник {work.get_full_name()} получает {work.get_total_income()}")


# 6-4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return self.speed

    def go(self):
        print(f"машина поехала")

    def stop(self):
        print(f"машина остановилась")

    def turn(self, direction):
        print(f"машина повернула {direction}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Текщая скорость {self.speed}, разрешенная 60! вы Превысили"
        else:
            return f"Текщая скорость {self.speed}"

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Текщая скорость {self.speed}, разрешенная 40! вы Превысили"
        else:
            return f"Текщая скорость {self.speed}"

class SportCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Текщая скорость {self.speed}, разрешенная 40! вы Превысили"
        else:
            return f"Текщая скорость {self.speed}"

class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Текщая скорость {self.speed}, разрешенная 40! вы Превысили"
        else:
            return f"Текщая скорость {self.speed}"

town_сar = TownCar(70, 'red', 'LADA', False)
work_сar = WorkCar(30, 'red', 'LADA', False)
sport_сar = SportCar(70, 'red', 'LADA', False)
police_сar = PoliceCar(70, 'red', 'LADA', True)

print(town_сar.show_speed())
work_сar.turn('Налево')




# 6_5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"“Запуск отрисовки.”")


class Pen(Stationery):
    def draw(self):
        print(f"“Запуск отрисовки. {self.title}”")


class Pencil(Stationery):
    def draw(self):
        print(f"“Рисуем: {self.title}”")


class Handle(Stationery):
    def draw(self):
        print(f"“Вырисовывает: {self.title}))”")


Pen('Обычная ручка').draw()
Handle('Красивая ручка').draw()
Pencil('Карандаш').draw()




