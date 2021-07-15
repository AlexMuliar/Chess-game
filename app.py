from game.boards.chess_board import ChessBoard
from game.chess_builders.chess960 import Chess960Builder
from game.chess_builders.classic_chess import ClassicChessBuilder
from game.chess_rules.abstract_rule import AbstractChessRules


if __name__ == '__main__':
    board = ChessBoard(size=(8, 8))
    board.fill_board(ClassicChessBuilder)
    print(board.pretty)
