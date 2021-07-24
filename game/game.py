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
from .players.abstract_player import AbcstractPlayer
from .utils.decorators import execute_until_result


COLORS = ["White", "Black"]


class MovePlaceHolder:
    def __str__(self) -> str:
        return 'x'


class Game:
    board = TypeValidatior(AbsctactBoard)

    _builder = TypeValidatior(AbstractBoardBuilder)
    _rules = TypeValidatior(AbstractChessRules)

    # TODO: make type validator for iterable structs

    def __init__(self, board: AbsctactBoard, buider: AbstractBoardBuilder, rules: AbstractChessRules, players: List[AbcstractPlayer]) -> None:
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


    def run(self):
        # TODO Make win condition
        while True:
            for player in self._players:
                player.update_ui(self.board.board)
                figure_position: Position = player.select_figure(self.board)
                moves: List[Position] = self._rules.get_moves_for_figure(self.board, figure_position)
                temp_board = deepcopy(self.board.board)
                for move in moves:
                    if self.board.get_item(move) is None:
                        temp_board[move.row][move.column] = MovePlaceHolder()
                player.update_ui(temp_board)
                new_coord = player.get_new_coord(moves)
                self.board.move_item(from_=figure_position, to_=new_coord)

