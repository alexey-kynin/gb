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
