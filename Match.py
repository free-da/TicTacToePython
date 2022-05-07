from Grid import Grid
from Symbol import Symbol


class Match:
    # public Grid grid;
    # public boolean playersTurn;
    # public boolean gameIsOver;
    # public String winner;
    # public int numberOfMoves;
    # public Symbol playerSymbol;
    # public Symbol botSymbol;

    def __init__(self, player_symbol):
        self.grid = Grid()
        self.player_symbol = player_symbol
        self.bot_symbol = Symbol.O if self.player_symbol == Symbol.X else Symbol.X;
        self.players_turn = bool(True)
        self.game_is_over = bool(False)
        self.number_of_moves = 0
        self.winner = ""