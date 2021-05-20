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

# print(cells1)
# print(cells1 + cells2)
# print(cells2 - cells1)
# print(cells2.make_order(5))
# print(cells1.make_order(10))
# print(cells1 / cells2)