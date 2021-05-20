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
