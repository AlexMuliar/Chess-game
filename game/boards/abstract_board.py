from abc import ABC, abstractmethod, ABCMeta
from typing import List, Tuple
from descriptors.board.board_size import BoardSize
from game_builders.abstract_builder import AbstractBoardBuilder


class AbsctactBoard(metaclass=ABCMeta):
    size = BoardSize()

    def __init__(self, size: Tuple[int, int]) -> None:
        self.size = size
        self.board = self._build_empty_board()


    def _build_empty_board(self) -> List[List]:
        board: List[List] = []
        for row in range(self.size[0]):
            board.append(list())
            for col in range(self.size[1]):
                board[-1].append(None)
        return board


    def fill_board(self, builder: AbstractBoardBuilder):
        self.board = builder.set_figures_to_board(self.board)

    def __repr__(self) -> str:
        return '\n'.join([
            str(line) for line in self.board
        ])
