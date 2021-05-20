# 7_2
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod  #определяем абстрактный метод, и потом в каждом дочернем классе его переопределяем
    def get_sq(self):
        pass

    @property
    def get_total_expense(self):
        return str(f'Общий расхода ткани: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def get_sq(self):
        return self.width / 6.5 + 0.5

    def __str__(self):
        return f'Расхода ткани на пальто {self.get_sq()}'

class Jacket(Clothes):
    def get_sq(self):
        return self.height * 2 + 0.3

    def __str__(self):
        return f'Расхода ткани на костюм {self.get_sq()}'

coat = Coat(10, 20)
jacket = Jacket(11, 22)
print(coat)
print(jacket)
print(coat.get_total_expense)
