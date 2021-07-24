from typing import List, Tuple

from game.chess_figures.abstract_figure import AbstractFigure
from rock import Rock
from bishop import Bishop
from position import Position


class Queen(AbstractFigure):
    def __init__(self) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Position, board_size:  Tuple[int, int]) -> List[Position]:
        return [
            *Bishop.get_moves(current_position, board_size),
            *Rock.get_moves(current_position, board_size)
        ]





