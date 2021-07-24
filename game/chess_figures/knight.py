from typing import List, Set, Tuple

from game.chess_figures.abstract_figure import AbstractFigure
from position import Position


class Knight(AbstractFigure):
    def __init__(self, ) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Position, board_size: Tuple[int, int]) -> List[Position]:
        moves = Knight._get_move_template()
        moves  = map(
            lambda x: Position(
                x.row + current_position.row,
                x.column + current_position.column
            ),
            moves
        )
        moves = Knight._filter_outer_moves(moves, board_size)
        return [[move] for move in moves]



    @staticmethod
    def _get_move_template() -> List[Position]:
        basic_moves: List[Position] = [
            Position(1, 2),
            Position(2, 1)
        ]
        return [
            *basic_moves,
            *Knight._make_mirror_moves(basic_moves, (1, -1)),
            *Knight._make_mirror_moves(basic_moves, (-1, 1)),
            *Knight._make_mirror_moves(basic_moves, (-1, -1)),
        ]



    @staticmethod
    def _make_mirror_moves(moves: List[Position], direction: Tuple[int, int]) -> List[Position]:
        new_moves: List[Position] = list()
        for move in moves:
            new_moves.append(Position(
                move.row * direction[0],
                move.column * direction[1]
            ))
        return new_moves

