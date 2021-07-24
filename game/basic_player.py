from position import Position

class Player:
    def __init__(self) -> None:
        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if self._color is None:
            self._color = value
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object attribute 'color' is read-only")


    def get_coord(self):
        # TODO Make user input validator
        x, y = [int(coord) for coord in input("(x y) >>> ").split()]
        return Position(x, y)
