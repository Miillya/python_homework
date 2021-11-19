class StationeryProducts:
    title: str
    _message = "start drawing"

    def draw(self):
        print(self._message)

class Pen(StationeryProducts):
    title = 'Pen'
    _message = f"{title} - writes in a notebook"

class Pencil(StationeryProducts):
    title = 'Pencil'
    _message = f"{title} - draws on paper"

class Marker(StationeryProducts):
    title = 'Marker'
    _message = f"{title} - writes on the board"

items = [Pen(), Pencil(), Marker()]

for item in items:
    item.draw()