from abc import ABCMeta, abstractstaticmethod, abstractmethod
from typing import List

from game.boards.abstract_board import AbsctactBoard, AbstractBoardBuilder
from game.type_descriptors.bool import Bool
from position import Postion


class AbstractChessRules(metaclass=ABCMeta):
    castling = Bool()
    def __init__(self, castling: bool=True) -> None:
        self.castling = castling

    def _is_check(self, board: AbsctactBoard) -> bool:
        raise NotImplementedError()


    def _is_mate(self, board: AbsctactBoard) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def _filter_moves(self, board: AbsctactBoard) -> List[Postion]:
        raise NotImplementedError()