from position import Position
from typing import List, Tuple
from game.chess_figures.abstract_figure import AbstractFigure



class Pawn(AbstractFigure):
    def __init__(self) -> None:
        super().__init__()


    @staticmethod
    def get_moves(current_position: Position, board_size: Tuple[int, int], direction=1) -> List[List[Position]]:
        moves: List[Position] = [Position(current_position.row + (direction * 2) , current_position.column)]
        for col_shift in range(-1, 2):
            moves.append(Position(
                current_position.row + direction,
                    current_position.column + col_shift
            ))
        result = [Pawn._filter_outer_moves(moves, board_size)]
        return result


class PawnState:
    def __init__(self, direction) -> None:
        self.direction = direction
        self.moved = False

    def get_moves(self, current_position: Position, board_size: Tuple[int, int]) -> List[List[Position]]:
        print(self)
        moves = Pawn.get_moves(current_position=current_position,\
            board_size=board_size, direction=self.direction)
        if self.moved:
            moves[0] = list(filter(
                lambda pos: pos.row == (current_position.row + self.direction),
                moves[0]
            ))
        self.moved = True
        return moves