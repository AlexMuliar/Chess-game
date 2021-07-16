from typing import List, Set, Tuple

from game.chess_figures.abstract_figure import AbstractFigure
from position import Postion


class Rock(AbstractFigure):
    def __init__(self) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Postion, board_size: Tuple[int, int]) -> List[Postion]:
        return list(
                Rock._get_vertical_moves(current_position, board_size) | \
                Rock._get_horizontal_moves(current_position, board_size)
        )


    @staticmethod
    def _get_vertical_moves(current_position: Postion, board_size: Tuple[int, int]) -> Set[Postion]:
        moves: List[Postion] = list()
        for row in range(board_size[0]):
            moves.append(
                Postion(row, current_position.column)
            )
        return set(moves)


    @staticmethod
    def _get_horizontal_moves(current_position: Postion, board_size: Tuple[int, int]) -> Set[Postion]:
        moves: List[Postion] = list()
        for col in range(board_size[1]):
            moves.append(
                Postion(current_position.row, col)
            )
        return set(moves)

