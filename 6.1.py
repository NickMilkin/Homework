from time import sleep


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый", "Желтый"]

    def running(self):
        i = 0
        while True:
            print(TrafficLight.__color[i % 4])
            if i % 4 == 0:
                sleep(7)
            elif i % 4 == 1 or i % 4 == 3:
                sleep(2)
            elif i % 4 == 2:
                sleep(5)
            i += 1

example = TrafficLight()
example.running()
