class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self, spec_grav, thick):
        return (self._length * self._width * spec_grav * thick) / 1000

road = Road(20, 5000)

print(road.get_weight(25,5))