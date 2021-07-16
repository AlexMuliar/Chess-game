from typing import List, Tuple

from game.chess_figures.abstract_figure import AbstractFigure
from rock import Rock
from bishop import Bishop
from position import Postion


class Queen(AbstractFigure):
    def __init__(self) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Postion, board_size:  Tuple[int, int]) -> List[Postion]:
        return list(
            set(Bishop.get_moves(current_position, board_size)) | \
                set(Rock.get_moves(current_position, board_size))
        )





