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


