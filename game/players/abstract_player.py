from abc import ABCMeta, abstractmethod
from string import ascii_lowercase
from typing import Tuple, List
from functools import wraps

from game.boards.abstract_board import AbsctactBoard
from position import Position

class AbcstractPlayer(metaclass=ABCMeta):
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


    def decode(self, code: str) -> Position:
        char_code = list(filter(
            lambda char: char.isalpha(),
            code.lower()
        ))[0]
        column = ascii_lowercase.index(char_code) if char_code else None
        number_code = list(filter(
            lambda char: char.isdigit(),
            code.lower()
        ))[0]
        row = int(number_code) if number_code else None
        return Position(row, column)


    def encode(self, postion: Position) -> str:
        return ''.join([
            ascii_lowercase[postion.column],
            str(postion.row)
        ])


    @abstractmethod
    def select_figure(self, board: AbsctactBoard) -> Position:
        raise NotImplementedError()


    @abstractmethod
    def get_new_coord(self, coords: List[Position]) -> Position:
        raise NotImplementedError()


    @abstractmethod
    def update_ui(self, board) -> None:
        raise NotImplementedError


    @staticmethod
    def _raise_error_if_not_color(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            if args[0].color is None:
                raise AttributeError(f"Set {args[0].__class__}.color first")
            else:
                return func(*args, **kwargs)
        return wrap
