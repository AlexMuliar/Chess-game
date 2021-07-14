from typing import List, Set, Tuple

from abstract_figure import AbstractFigure
from figure_color import WhiteFigure, BlackFigure
from position import Postion



class Knight(AbstractFigure):
    def __init__(self, ) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Postion, board_size: Tuple[int, int]) -> List[Postion]:
        moves = Knight._get_move_template()
        moves  = map(
            lambda x: Postion(
                x.row + current_position.row,
                x.column + current_position.column
            ),
            moves
        )
        moves = Knight._filter_outer_moves(moves, board_size)
        return moves


    @staticmethod
    def _get_move_template() -> List[Postion]:
        basic_moves: List[Postion] = [
            Postion(1, 2),
            Postion(2, 1)
        ]
        return [
            *basic_moves,
            *Knight._make_mirror_moves(basic_moves, (1, -1)),
            *Knight._make_mirror_moves(basic_moves, (-1, 1)),
            *Knight._make_mirror_moves(basic_moves, (-1, -1)),
        ]



    @staticmethod
    def _make_mirror_moves(moves: List[Postion], direction: Tuple[int, int]) -> List[Postion]:
        new_moves: List[Postion] = list()
        for move in moves:
            new_moves.append(Postion(
                move.row * direction[0],
                move.column * direction[1]
            ))
        return new_moves

