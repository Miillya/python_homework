from time import sleep

class TrafficLight:
    colors = ("red", "yellow", "green")
    pause = (7, 2, 10)

    def __init__(self):
        self.__color = "green"

    def running(self):
        while True:
            for x in self.colors:
                self.__color = x
                print(self.__color)
                sleep(self.pause[self.colors.index(self.__color)])

traffic_light = TrafficLight()
traffic_light.running()