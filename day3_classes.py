class Character:
    def __init__(self, x=0, y=0, name=""):
        self._x = x
        self._y = y
        self._name = name

    def move_character(self, x, y):
        self._x += x
        self._y += y

    def get_location(self):
        return "X: " + str(self._x) + " Y: " + str(self._y)

    def get_name(self):
        return self._name


class HousePresents:
    def __init__(self, location, presents=0):
        self._location = location
        self._presents = presents

    def add_present(self):
        self._presents += 1

    def get_presents(self):
        return self._presents

    def get_location(self):
        return self._location
