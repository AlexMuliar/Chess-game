from typing import List, Set, Tuple

from game.chess_figures.abstract_figure import AbstractFigure
from position import Position



class King(AbstractFigure):
    def __init__(self) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Position, board_size: Tuple[int, int]) -> List[List[Position]]:
        moves: List[Position] = list()
        for row in range(current_position.row - 1, current_position.row + 2):
            for col in range(current_position.column - 1, current_position.column + 2):
                print(row, col)
                moves.append(Position(row, col))
        moves = King._filter_outer_moves(moves, board_size)
        return [[move] for move in moves]




