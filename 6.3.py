class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))


example = Position('Саша', 'Сашин', 'Президент', 5000, 1000)
example.get_full_name()
example.get_total_income()
