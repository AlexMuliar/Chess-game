import random

from copy import copy, deepcopy
from typing import List

from position import Position
from game.chess_figures.abstract_figure import AbstractFigure

from game.boards.abstract_board import AbsctactBoard
from game.chess_builders.abstract_builder import AbstractBoardBuilder
from game.chess_rules.abstract_rule import AbstractChessRules
from type_descriptors.type_validation import TypeValidatior
from .chess_figures.figure_color import BlackFigure, WhiteFigure
from .basic_player import Player
from .utils.decorators import execute_until_result
from .utils.console_utils import clear_console


COLORS = ["White", "Black"]


class MovePlaceHolder:
    def __str__(self) -> str:
        return 'x'


class Game:
    board = TypeValidatior(AbsctactBoard)

    _builder = TypeValidatior(AbstractBoardBuilder)
    _rules = TypeValidatior(AbstractChessRules)

    # TODO: make type validator for iterable structs

    def __init__(self, board: AbsctactBoard, buider: AbstractBoardBuilder, rules: AbstractChessRules, players: List[Player]) -> None:
        self.board = board
        self._builder = buider
        self._rules = rules
        self._players = players
        self._build_board()
        self._set_players_colors()


    def _build_board(self) -> None:
        self.board.board = self._builder.set_figures_to_board(self.board.board)


    def _set_players_colors(self) -> None:
        random.shuffle(self._players)
        for player, color in zip(self._players, COLORS):
            player.color = color
        self._players = sorted(self._players, key=lambda player: COLORS.index(player.color))


    def print_board(self, board: List[List[AbstractFigure]], player: Player) -> None:
        # clear_console()
        print(f"{player.color} turn")
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
        print('  ' + ' '.join([str(number) for number in range(self.board.size[1])]))


    def run(self):
        # TODO Make win condition
        while True:
            for player in self._players:
                self.print_board(self.board.board, player)
                figure_position: Position = self._choose_figure(player)
                moves: List[Position] = self._rules.get_moves_for_figure(self.board, figure_position)

                temp_board = deepcopy(self.board.board)
                for move in moves:
                    if self.board.get_item(move) is None:
                        temp_board[move.row][move.column] = MovePlaceHolder()
                self.print_board(temp_board, player)
                while (new_coord:=player.get_coord()) not in moves:
                    print("Coords invalid for this figure")
                self.board.move_item(from_=figure_position, to_=new_coord)


    @execute_until_result
    def _choose_figure(self, player: Player) -> Position:
        figure_position = player.get_coord()
        if not self._is_coord_inside_board(figure_position):
            raise ValueError(f"Coord cannot be grater than {self.board.size}")

        if not isinstance(self.board.get_item(figure_position), AbstractFigure):
            print(isinstance(self.board.get_item(figure_position), AbstractFigure))
            raise AttributeError(f'Field {figure_position} is empty')
        figure  = self.board.get_item(figure_position)
        if figure.color != player.color:
            raise AttributeError(f'Field {figure_position} contain not Player\'s figure')

        return figure_position




    def _is_coord_inside_board(self, figure_position: Position) -> bool:
        if figure_position.row >= self.board.size[0] or \
                    figure_position.column >= self.board.size[1]:
                return False
        return True
