from game.position import Postion
from typing import List, Tuple
from abstract_figure import AbstractFigure



class Pawn(AbstractFigure):
    def __init__(self) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Postion, board_size: Tuple[int, int], direction=1) -> List[Postion]:
        moves: List[Postion] = [Postion(current_position.row + (direction * 2) , current_position.column)]
        while True:
            for col_shift in range(3):
                moves.append(Postion(
                    current_position.row + direction,
                     current_position.column + col_shift
                ))
            return Pawn._filter_outer_moves(moves, board_size)
