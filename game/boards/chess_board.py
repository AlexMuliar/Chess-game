from game.chess_figures.abstract_figure import AbstractFigure
from game import boards
from typing import List, Tuple

import sys
import os

from abstract_board import AbsctactBoard

from position import Postion
from chess_builders.abstract_builder import AbstractBoardBuilder

class ChessBoard(AbsctactBoard):
    @property
    def pretty(self) -> str:
        return '\n'.join(['  '.join([
            str(item) if item else '·' for item in line
        ]) for line in self.board])


if __name__ == '__main__':
    a = ChessBoard(size=(8, 8))
    print(a.__repr__())