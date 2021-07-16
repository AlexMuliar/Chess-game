from game.chess_rules import classic_chess
from typing import List

from game.chess_builders.abstract_builder import AbstractBoardBuilder
from game.chess_figures.abstract_figure import AbstractFigure
from game.chess_figures.colored_figures_fabric import (WhiteKing,
                BlackKing, WhiteQueen, BlackQueen, WhiteRock,
                BlackRock, WhiteBishop, BlackBishop, WhiteKnight,
                BlackKnight, WhitePawn, BlackPawn)


class ClassicChessBuilder(AbstractBoardBuilder):
    @staticmethod
    def set_figures_to_board(board: List[List[AbstractFigure]]) -> List[List[AbstractFigure]]:
        if (len(board), len(board[0])) != (8, 8):
            raise ValueError(f"Board size must be 8x8, no {board.size}")
        board[0] = [
            BlackRock(), BlackKnight(), BlackBishop(), BlackQueen(), BlackKing(),
            BlackBishop(), BlackKnight(), BlackRock()
        ]
        board[1] = [BlackPawn() for _ in range(8)]
        board[-2] = [WhitePawn() for _ in range(8)]
        board[-1] = [
            WhiteRock(), WhiteKnight(), WhiteBishop(), WhiteQueen(), WhiteKing(),
            WhiteBishop(), WhiteKnight(), WhiteRock()
        ]
        return board


