from typing import List, Set, Tuple

from game.chess_figures.abstract_figure import AbstractFigure
from position import Position


class Rock(AbstractFigure):
    def __init__(self) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Position, board_size: Tuple[int, int]) -> List[List[Position]]:
        return [
                *Rock._get_vertical_moves(current_position, board_size),
                *Rock._get_horizontal_moves(current_position, board_size)
        ]

    @staticmethod
    def _get_vertical_moves(current_position: Position, board_size: Tuple[int, int]) -> List[Position]:
        moves: List[List[Position]] = list([])
        for row in range(board_size[0]):
            if row <= current_position.row:
                moves.append([])
            moves[-1].append(
                Position(row, current_position.column)
            )
        return moves


    @staticmethod
    def _get_horizontal_moves(current_position: Position, board_size: Tuple[int, int]) -> List[Position]:
        moves: List[List[Position]] = list([])
        for col in range(board_size[1]):
            if col <= current_position.column:
                moves.append([])
            moves[-1].append(
                Position(current_position.row, col)
            )
        return moves

