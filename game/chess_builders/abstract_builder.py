from abc import ABC, ABCMeta, abstractstaticmethod
from typing import List

from game.chess_figures.abstract_figure import AbstractFigure


class AbstractBoardBuilder():
    @abstractstaticmethod
    def set_figures_to_board(board: List[List[AbstractFigure]]) -> List[List[AbstractFigure]]:
        raise NotImplementedError()


