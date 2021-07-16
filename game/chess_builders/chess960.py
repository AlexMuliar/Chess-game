import random

from typing import List
from .abstract_builder import AbstractBoardBuilder
from classic_chess import ClassicChessBuilder
from game.chess_figures.abstract_figure import AbstractFigure


class Chess960Builder(AbstractBoardBuilder):
    @staticmethod
    def set_figures_to_board(board: List[List[AbstractFigure]]) -> List[List[AbstractFigure]]:
        if (len(board), len(board[0])) != (8, 8):
            raise ValueError(f"Board size must be 8x8, no {board.size}")
        board = ClassicChessBuilder.set_figures_to_board(board)
        seed = random.randint(0, 1000)
        random.Random(seed).shuffle(board[0])
        random.Random(seed).shuffle(board[-1])
        return board

