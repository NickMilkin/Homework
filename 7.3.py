class Cell:
    def __init__(self, count):
        self._count = count

    def __add__(self, other):
        return Cell(self._count + other._count)

    def __sub__(self, other):
        if self._count > other._count:
            return Cell(self._count - other._count)

        print(f"{self._count} - {other._count}: отрицательное значение или ноль")
        return ""

    def __mul__(self, other):
        return Cell(self._count * other._count)

    def __truediv__(self, other):
        return Cell(self._count // other._count)

    def make_order(self, n):
        rows, tail = self._count // n, self._count % n
        return f'\n'.join(['*' * n] * rows + (['*' * tail] if tail else []))

    def __str__(self):
        return f"Клетка состоит из {self._count} ячеек"


c_1 = Cell(3)
c_2 = Cell(10)

print(c_1)
print(c_2)

print(c_1 + c_2)

print(c_1 - c_2)
print(c_2 - c_1)

print(c_1 * c_2)
print(c_1 / c_2)

print((c_1 * c_2).make_order(10))
