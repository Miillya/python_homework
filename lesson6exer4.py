class Car:
    def __init__(self, speed, color, name, police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = police

    def go(self):
        print(f"{self.name}: go")

    def stop(self):
        print(f"{self.name}: stop")

    def turn(self, direction):
        print(f"{self.name}: turned - {direction}")

    def show_speed(self):
        print(f"{self.name}: speed = {self.speed} km/h")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}: over speed")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{ self.name}: over speed")

class PoliceCar(Car):
    is_police: bool = True

cars = [
    SportCar(240, 'red', 'Audi'),
    TownCar(180, 'green', 'Kia'),
    WorkCar(80, 'yellow', 'Pego'),
    PoliceCar(170, 'black', 'Ford')
]

cars[0].go()
cars[0].turn("right")
cars[0].stop()

for car in cars:
    car.show_speed()