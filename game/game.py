import random

from copy import copy, deepcopy
from typing import List

from game.position import Postion
from game.chess_figures.abstract_figure import AbstractFigure

from game.boards.abstract_board import AbsctactBoard
from game.chess_builders.abstract_builder import AbstractBoardBuilder
from game.chess_rules.abstract_rule import AbstractChessRules
from type_descriptors.type_validation import TypeValidatior
from .chess_figures.figure_color import BlackFigure, WhiteFigure
from .basic_player import Player
from .utils.decorators import execute_until_valid
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


    def print_board(self, board: List[List[AbstractFigure]]) -> None:
        # clear_console()
        for i, line in enumerate(board):
            print(i, end=' ')
            line = list(map(
                lambda x: '·' if x is None else str(x),
                line
            ))
            print(' '.join(line))
        print('  ' + ' '.join([str(number) for number in range(self.board.size[1])]))


    def run(self):
        # TODO Make win condition
        while True:
            for player in self._players:
                self.print_board(self.board.board)
                print(f"{player.color} turn")
                figure_position: Postion = self._choose_figure(player)
                figure: AbstractFigure = self.board.board[figure_position.row][figure_position.column]
                moves: List[Postion] = figure.get_moves(figure_position, self.board.size)
                temp_board = deepcopy(self.board.board)
                for move in moves:
                    if self.board.board[move.row][move.column] is None:
                        temp_board[move.row][move.column] = MovePlaceHolder()
                self.print_board(temp_board)
                new_coord = player.get_coord()
                self.board.board[new_coord.row][new_coord.column], self.board.board[figure_position.row][figure_position.column] = \
                    self.board.board[figure_position.row][figure_position.column], self.board.board[new_coord.row][new_coord.column]



    @execute_until_valid
    def _choose_figure(self, player: Player) -> Postion:
        figure_position = player.get_coord()
        if not self._is_coord_inside_board(figure_position):
            raise ValueError(f"Coord cannot be grater than {self.board.size}")

        if not isinstance(self.board.board[figure_position.row][figure_position.column], AbstractFigure):
            print(isinstance(self.board.board[figure_position.row][figure_position.column], AbstractFigure))
            raise AttributeError(f'Field {figure_position} is empty')
        figure  = self.board.board[figure_position.row][figure_position.column]
        if figure.color != player.color:
            raise AttributeError(f'Field {figure_position} contain not Player\'s figure')

        return figure_position




    def _is_coord_inside_board(self, figure_position: Postion) -> bool:
        if figure_position.row >= self.board.size[0] or \
                    figure_position.column >= self.board.size[1]:
                return False
        return True
