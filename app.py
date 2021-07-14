from game.boards.chess_board import ChessBoard
from game.game_builders.chess960 import Chess960Builder
from game.game_builders.classic_chess import ClassicChessBuilder


if __name__ == '__main__':
    board = ChessBoard(size=(8, 8))
    board.fill_board(Chess960Builder)
    print(board.pretty)
