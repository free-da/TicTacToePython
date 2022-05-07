import random

import GameboardDrawer
from WinChecker import WinChecker


class MatchController:
    # private Match match;
    # private Random randomizerForBotMoves = new Random();

    def __init__(self, match):
        self.match = match

    def start_match(self):
        self.start_game_loop()
        self.announce_end_of_game()
        self.announce_winner()

    def start_game_loop(self):
        while self.is_game_over() == bool(False):
            self.next_move()

    def is_game_over(self):
        if self.someone_won():
            self.match.game_is_over = bool(True)
        if self.match.number_of_moves == (self.match.grid.number_of_columns * self.match.grid.number_of_rows):
            self.match.game_is_over = bool(True)
            self.someone_won()
        return self.match.game_is_over

    def someone_won(self):
        if WinChecker.check_if_either_won(self.match.player_symbol, self.match.grid):
            self.match.winner = "player"
            return bool(True)
        if WinChecker.check_if_either_won(self.match.bot_symbol, self.match.grid):
            self.match.winner = "bot"
            return bool(True)
        return bool(False)

    def next_move(self):
        if self.match.players_turn:
            self.player_makes_next_move()
        else:
            self.bot_makes_next_move()
        self.match.number_of_moves += 1
        GameboardDrawer.draw_gameboard(self.match.grid)

    def bot_makes_next_move(self):
        row_index = random.randrange(self.match.grid.number_of_rows)
        column_index = random.randrange(self.match.grid.number_of_columns)
        if self.match.grid.check_if_field_is_empty(row_index, column_index):
            self.match.grid.set_field_value(row_index, column_index, self.match.bot_symbol);
            self.match.players_turn = bool(True)
        else:
            self.bot_makes_next_move()

    def player_makes_next_move(self):
        user_input = input(">_")
        if self.coordinate_input_is_valid(user_input):
            self.match.grid.set_field_value(self.find_row_index(user_input), self.find_column_index(user_input), self.match.player_symbol)
        else:
            print("Please, play by the rules. Try again.")
            self.player_makes_next_move()
        self.match.players_turn = bool(False)

    def announce_winner(self):
        if self.match.game_is_over and self.someone_won():
            if self.match.winner == "player":
                print("You won.")
            elif self.match.winner == ("bot"):
                print("You lost. The machine is superior.")
            else:
                print("Tied. Everybody loses.")


    def announce_end_of_game(self):
        print("Game is over.")

    def find_column_index(self, user_input):
        second_letter = user_input[1]
        coordinates_helper_columns = "ABCDEFG"
        coordinates_helper_columns = coordinates_helper_columns[0:self.match.grid.number_of_columns]
        return coordinates_helper_columns.index(second_letter.upper())

    def find_row_index(self, user_input):
        first_letter = user_input[0]
        coordinates_helper_rows = "123456";
        coordinates_helper_rows = coordinates_helper_rows[0:self.match.grid.number_of_rows]
        return coordinates_helper_rows.index(first_letter.upper())

    def coordinate_input_is_valid(self, user_input):
        if len(user_input) == 2:
            column_index = self.find_column_index(user_input)
            row_index = self.find_row_index(user_input)
            return not (column_index < 0 or row_index < 0 or not self.match.grid.check_if_field_is_empty(row_index, column_index))
        return bool(False)