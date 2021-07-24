from abc import ABCMeta, abstractstaticmethod, abstractmethod
from typing import List

from game.boards.abstract_board import AbsctactBoard, AbstractBoardBuilder
from game.type_descriptors.bool import Bool
from position import Position


class AbstractChessRules(metaclass=ABCMeta):
    castling = Bool()
    def __init__(self, castling: bool=True) -> None:
        self.castling = castling
        self._left_castling = True
        self._right_castling = True


    def _is_check(self, board: AbsctactBoard) -> bool:
        raise NotImplementedError()


    def _is_mate(self, board: AbsctactBoard) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_moves_for_figure(self, board: AbsctactBoard, position: Position) -> List[Position]:
        raise NotImplementedError()