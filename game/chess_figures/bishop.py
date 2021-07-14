from typing import List, Set, Tuple, Iterator

from abstract_figure import AbstractFigure
from figure_color import WhiteFigure, BlackFigure
from position import Postion


class Bishop(AbstractFigure):
    def __init__(self) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Postion, board_size: Tuple[int, int]) -> List[Postion]:
        start_bottom_position = Bishop._get_down_start_position(current_position, board_size)
        start_side_position = Bishop._get_side_start_position(current_position, board_size)
        return list(Bishop._get_diagonal_moves(current_position, board_size,
                start_bottom_position, zip(range(board_size[0]), range(board_size[1]))
        ) | Bishop._get_diagonal_moves(current_position, board_size,
                start_side_position, zip(range(0, -start_side_position.row-1, -1), range(board_size[1] - start_side_position.column))
        ))



    def _get_diagonal_moves(self, current_position: Postion, board_size: Tuple[int, int],
                         start_position: Postion, diagonal: zip) -> Set[Postion]:
        moves: List[Postion] = list()
        for row, col in diagonal:
            new_position = Postion(
                start_position.row + row,
                start_position.column + col,
            )
            if 0 <= new_position.row < board_size[0] and \
                    0 <= new_position.column < board_size[1]:
                moves.append(new_position)
        return set(moves)


    @staticmethod
    def _get_down_start_position(current_position: Postion, board_size: Tuple[int, int]) -> Postion:
        if current_position.row >= current_position.column:
            start_row = current_position.row - current_position.column
            start_col = 0
        else:
            start_row = 0
            start_col = current_position.column - current_position.row
        start_position = Postion(
            start_row, start_col
        )
        return start_position



    @staticmethod
    def _get_side_start_position(current_position: Postion, board_size: Tuple[int, int]) -> Postion:
        distance_to_left_border = current_position.column
        distance_to_bottom_border = board_size[0] - current_position.row - 1

        if distance_to_left_border < distance_to_bottom_border:
            start_row = current_position.row + distance_to_left_border
            start_col = 0
        else:
            start_row = board_size[0] - 1
            start_col =  current_position.column - distance_to_bottom_border
        start_position = Postion(
            start_row, start_col
        )
        return start_position


