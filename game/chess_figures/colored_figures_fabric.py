from typing import Tuple
from position import Position
from game.chess_figures.abstract_figure import AbstractFigure
from ..chess_figures.pawn import Pawn, PawnState
from ..chess_figures.bishop import Bishop
from ..chess_figures.king import King
from ..chess_figures.queen import Queen
from ..chess_figures.rock import Rock
from ..chess_figures.knight import Knight

from figure_color import AbstractFigureColor, WhiteFigure, BlackFigure

import types


FIGURES = [
    King, Queen, Rock, Bishop,
    Knight, Pawn
]

def generate_colored_figure(figure_class: AbstractFigure, color: AbstractFigureColor, code: int):
    cls_ = type(f"{color().color}{figure_class().__class__.__name__}",
            (figure_class, color), (dict(icon=chr(code)))
    )
    cls_.__str__ = lambda x: x.icon
    cls_.__str__.__name__ = '__str__'
    globals()[cls_().__class__.__name__] = cls_


for index_, code in enumerate(range(0x2654, 0x2659)):
    for color, shift in zip([BlackFigure, WhiteFigure], [0, 6]):
        generate_colored_figure(FIGURES[index_], color, code+shift)

for color, shift, direction in zip([BlackFigure, WhiteFigure], [0, 6], [1, -1]):
    cls_ = type(f"{color().color}{Pawn().__class__.__name__}",
                (PawnState, color),
                (dict(icon=chr(0x2659 + shift), direction=direction, color=color().color))
        )
    cls_.__str__ = lambda x: x.icon
    cls_.__str__.__name__ = '__str__'
    globals()[cls_().__class__.__name__] = cls_
