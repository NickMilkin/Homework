class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def mass(self):
        self.weight = 25
        self.thickness = 5
        print(f"{self._length * self._width * self.weight * self.thickness / 1000} тонн")


example = Road(20, 5000)
example.mass()
