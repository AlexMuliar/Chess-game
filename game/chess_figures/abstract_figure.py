from typing import List, Tuple, Any, Dict
from abc import ABC, abstractmethod, abstractstaticmethod, ABCMeta

from descriptors.chess_icon import ChessIconCode
from position import Postion



class AbstractFigure(metaclass=ABCMeta):
    icon = ChessIconCode()
    __slots__ = ()

    def __init__(self) -> None:
        super().__init__()


    @abstractstaticmethod
    def get_moves(self, current_position: Postion, board_size:  Tuple[int, int]) -> List[Postion]:
        raise NotImplementedError()


    @staticmethod
    def _filter_outer_moves(moves: List[Postion], board_size: Tuple[int, int]) -> List[Postion]:
        return list(filter(
            lambda x: 0 <= x.row < board_size[0] and \
                        0 <= x.column < board_size[1],
            moves
        ))