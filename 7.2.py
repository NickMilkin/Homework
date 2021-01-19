class Tissue:
    def __init__(self, x):
        self.x = x

    def for_coat(self):
        return round(self.x / 6.5 + 0.5, 3)

    def for_suit(self):
        return round(self.x * 2 + 0.3, 3)

    @property
    def for_all(self):
        return str(f'Всего потребуется: {round((self.x / 6.5 + 0.5) + (self.x * 2 + 0.3), 3)}')


class Coat(Tissue):
    def __init__(self, x):
        super().__init__(x)
        self.forcoat = round(self.x / 6.5 + 0.5, 3)

    def __str__(self):
        return f'Для пальто: {self.forcoat}'


class Suit(Tissue):
    def __init__(self, x):
        super().__init__(x)
        self.forsuit = round(self.x * 2 + 0.3, 3)

    def __str__(self):
        return f'Для костюма: {self.forsuit}'

coat = Coat(4)
suit = Suit(2)
print(coat)
print(suit)