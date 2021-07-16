from game.boards.chess_board import ChessBoard
from game.chess_builders.chess960 import Chess960Builder
from game.chess_builders.classic_chess import ClassicChessBuilder
from game.chess_rules.classic_chess import ClassicChessRules
from game.chess_rules.abstract_rule import AbstractChessRules

from game.game import Game
from game.basic_player import Player

if __name__ == '__main__':
    game = Game(
        ChessBoard((8, 8)),
        Chess960Builder(),
        ClassicChessRules(),
        [Player(), Player()]
    )
    print(game.run())
