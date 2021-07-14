from abc import ABC, ABCMeta
from typing import AbstractSet


class AbstractFigureColor(metaclass=ABCMeta):
    def __init__(self, color) -> None:
        super().__init__()
        self.color = color


class WhiteFigure(AbstractFigureColor):
    def __init__(self) -> None:
        super().__init__("White")


class BlackFigure(AbstractFigureColor):
    def __init__(self) -> None:
        super().__init__("Black")