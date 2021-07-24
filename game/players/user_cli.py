
from string import ascii_uppercase
from typing import List

from game.chess_figures.abstract_figure import AbstractFigure
from game.boards.abstract_board import AbsctactBoard
from game.players.abstract_player import AbcstractPlayer
from position import Position
from utils.decorators import execute_until_result
from utils.console_utils import clear_console



class UserCLI(AbcstractPlayer):
    def __init__(self) -> None:
        super().__init__()


    @AbcstractPlayer._raise_error_if_not_color
    def select_figure(self, board: AbsctactBoard) -> Position:
        return execute_until_result(self._select_figure)(board)


    @AbcstractPlayer._raise_error_if_not_color
    def get_new_coord(self, coords: List[Position]) -> Position:
        print("Awaible moves: ", 
            ' '.join(self.encode(coord) for coord in coords))

        while not (new_coord:=execute_until_result(self.decode)(input("Your move >>> "))) in coords:
            print('Unawaible move')
        return new_coord


    def update_ui(self, board: List[List[Position]]) -> None:
        clear_console()
        print(self.color)
        for i, line in enumerate(board):
            print(i, end=' ')
            out_line: str = ''
            for j, item in enumerate(line):
                if item is None:
                    if (i + j) % 2:
                        out_line += '·'
                    else:
                        out_line += ' '
                else:
                    out_line += str(item)
            print(' '.join(out_line))
        last_line = list(ascii_uppercase[:len(board[0])])
        print('  ' + ' '.join(last_line))


    def _select_figure(self,  board: AbsctactBoard) -> Position:
        figure_position = execute_until_result(self.decode)(input("Your move >>> "))

        if not self._is_coord_inside_board(figure_position, board):
            raise ValueError(f"Coord cannot be grater than {board.size}")

        if not isinstance(board.get_item(figure_position), AbstractFigure):
            print(isinstance(board.get_item(figure_position), AbstractFigure))
            raise AttributeError(f'Field {self.encode(figure_position)} is empty')
        figure  = board.get_item(figure_position)
        if figure.color != self.color:
            raise AttributeError(f'Field {self.encode(figure_position)} contain not AbcstractPlayer\'s figure')

        return figure_position


    def _is_coord_inside_board(self, figure_position: Position, board: AbsctactBoard) -> bool:
        if figure_position.row >= board.size[0] or \
                    figure_position.column >= board.size[1]:
                return False
        return True