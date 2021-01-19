class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.speed}', end=' ')

        if self.speed > 40:
            return f'{self.name} превышает скоростной лимит'
        else:
            return f'{self.name} в пределах лимита'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.speed}', end=' ')

        if self.speed > 60:
            return f'{self.name} превышает скоростной лимит'
        else:
            return f'{self.name} в пределах лимита'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская машина'
        else:
            return f'{self.name} - не полицейская машина'


example_s = SportCar(250, 'Красная', 'Ferrari', False)
example_t = TownCar(30, 'Черная', 'Toyota', False)
example_w = WorkCar(80, 'Белая', 'Honda', False)
example_p = PoliceCar(60, 'Синяя', 'Жигули', True)

print(example_s.show_speed())
print(example_t.show_speed())
print(example_w.show_speed())

print(example_p.police())
print(example_p.show_speed())

print(f'Началось движение: '
      f'{example_w.go()}, {example_p.go()}, {example_s.go()}, {example_t.go()}, '
      f'{example_w.turn_left()}, {example_t.turn_right()}, {example_s.stop()}')
