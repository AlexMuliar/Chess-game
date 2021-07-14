from abc import ABCMeta, abstractstaticmethod
from typing import List

from chess_figures.abstract_figure import AbstractFigure



class AbstractBoardBuilder(metaclass=ABCMeta):
    @abstractstaticmethod
    def set_figures_to_board(board: List[List[AbstractFigure]]) -> List[List[AbstractFigure]]:
        raise NotImplemented()
