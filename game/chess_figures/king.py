from typing import List, Set, Tuple

from game.chess_figures.abstract_figure import AbstractFigure
from position import Postion



class King(AbstractFigure):
    def __init__(self) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Postion, board_size: Tuple[int, int]) -> List[Postion]:
        moves: List[Postion] = list()
        for row in range(current_position.row - 1, current_position.row + 2):
            for col in range(current_position.column - 1, current_position.column + 2):
                print(row, col)
                moves.append(Postion(row, col))
        moves = King._filter_outer_moves(moves, board_size)
        return moves




