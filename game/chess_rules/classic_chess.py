from typing import List

from .abstract_rule import AbstractChessRules
from boards.abstract_board import AbsctactBoard 
from position import Postion


class ClassicChessRules(AbstractChessRules):
    def __init__(self, castling: bool=True) -> None:
        super().__init__(castling=castling)


    def _filter_moves(self, board: AbsctactBoard) -> List[Postion]:
        return list()

