from abc import ABCMeta, abstractstaticmethod, abstractmethod

from game.boards.abstract_board import AbstractBoardBuilder
from game.type_descriptors.bool import Bool



class AbstractChessRules(metaclass=ABCMeta):
    castling = Bool()
    def __init__(self, castling: bool=True) -> None:
        self.castling = castling

    @abstractmethod
    def filter_moves(self, board: AbstractBoardBuilder):
        raise NotImplementedError()