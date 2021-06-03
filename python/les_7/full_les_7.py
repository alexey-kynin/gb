# 7-1

user_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
user_list_2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

class Matrix:

    def __init__(self, user_list):
        self.user_list = user_list

    def __str__(self):
        return self.__get_res(self.user_list)

    def __add__(self, other):
        for i in range(0, 3): #я знаю что матрица 3 на 3, но если мы не знаем кол-во строк и строк то можно range(len(self.user_list))
            for j in range(0, 3): # а тут range(len(self.user_list))[0] кол-во столбцов
                result[i][j] = self.user_list[i][j] + other.user_list[i][j]

        return self.__get_res(result)

    def __get_res(self, output_list):
        return '\n'.join(
            ['  '.join(map(str, el)) for el in output_list]
        )


mat_1 = Matrix(user_list_1)
mat_2 = Matrix(user_list_2)
print(mat_1)
print(mat_2)
print(f"Результат сложения матриц: \n{mat_1 + mat_2}")

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

#7-3
class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):
        return f'Клеток {self.number * "[]"}: {self.number} шт.'

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        result = self.number - other.number
        return Cell(result) if result > 0 else f'Разница в кол-ве клеток отрицательна {result}'

    def __mul__(self, other):
        return Cell(int(self.number) * int(other.number))

    def __truediv__(self, other):
        result = self.number / other.number
        return Cell(round(result)) if result > 1 else f'Результат делени кол-ва клеток меньше 1 и равен {result}'


    def make_order(self, num_of_cells):
        row = ''
        for i in range(int(self.number / num_of_cells)):
            row += f'{"[]" * num_of_cells} \n'
        row += f'{"[]" * (self.number % num_of_cells)}'
        return row

cell_one = Cell(9)
cell_two = Cell(3)
print(cell_one + cell_two)
print(cell_two - cell_one)
print(cell_one * cell_two)
print(cell_one / cell_two)

print(cell_one.make_order(3))
print(cell_two.make_order(2))