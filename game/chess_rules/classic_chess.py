from game.chess_figures.bishop import Bishop
from game.chess_figures.queen import Queen
from game.chess_figures.rock import Rock
from game.chess_figures.figure_color import WhiteFigure
from game.utils.distance import euclidian
from game.chess_figures.abstract_figure import AbstractFigure
from typing import List, Tuple

from .abstract_rule import AbstractChessRules
from ..boards.abstract_board import AbsctactBoard 
from position import Position
from ..chess_figures.king import King
from ..chess_figures.pawn import Pawn
from ..chess_figures.knight import Knight

from time import sleep
from copy import deepcopy


class ClassicChessRules(AbstractChessRules):
    def __init__(self, castling: bool=True) -> None:
        super().__init__(castling=castling)


    def get_moves_for_figure(self, board: AbsctactBoard,\
                            position: Position) -> List[Position]:
        figure: AbstractFigure = board.get_item(position)
        moves: List[Position] = figure.get_moves(position, board.size)
        moves.extend(self._get_castling_moves(position, figure))
        moves = self._filtre_moves(moves, position, figure, board)
        return moves


    def _get_castling_moves(self, position: Position, figure: AbstractFigure) -> List[Position]:
        moves: List[Position] = []
        if isinstance(figure, King) and self.castling:
            if self._left_castling:
                moves.append([Position(position.row, position.column - 2)])
            if self._right_castling:
                moves.append([Position(position.row, position.column + 2)])
        return moves


    def _filtre_moves(self, moves: List[Position], figure_position: Position,\
                            figure: AbstractFigure, board: AbsctactBoard) -> List[Position]:

        if isinstance(figure, Pawn):
            return self._filter_pawn_moves(moves, figure_position, board)

        out_moves: List[Position] = list()
        for move in moves:
            if isinstance(figure, (Queen, Bishop, Rock)):
                branches = self._build_moves_branches(move, figure_position)
            else:
                branches = moves
            for branch in branches:
                for position in branch:
                    item = board.get_item(position)
                    if item is figure:
                        continue
                    if isinstance(item, AbstractFigure):
                        if figure.color != item.color:
                            out_moves.append(position)
                        break
                    out_moves.append(position)
        return out_moves



    def _filter_pawn_moves(self, moves: List[Position], position: Position, board: AbsctactBoard) -> List[Position]:
        out_moves: List[Position] = list(filter(
            lambda move: move.column == position.column,
            moves[0]
        ))
        else_moves: List[Position] = list(filter(
            lambda move: move.column != position.column,
            moves[0]
        ))
        figure = board.get_item(position)
        for move in else_moves:
            item = board.get_item(move)
            if isinstance(item, AbstractFigure) and item.color != figure.color:
                out_moves.append(move)

        return out_moves



    def _build_moves_branches(self, moves: List[Position], position: Position) -> List[List[Position]]:
        branches = [[]]
        sorted_moves = sorted(moves, key=lambda x: euclidian(position, x))
        curr_pos = sorted_moves.pop(0)
        while len(sorted_moves):
            sorted_moves = sorted(sorted_moves, key=lambda x: euclidian(curr_pos, x))
            if euclidian(sorted_moves[0], curr_pos) <= 1.5:
                curr_pos = sorted_moves.pop(0)
                branches[-1].append(curr_pos)
            else:
                branches.append([])
                curr_pos = position
        return branches