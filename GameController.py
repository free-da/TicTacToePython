from GameboardDrawer import GameboardDrawer
from Match import Match
from MatchController import MatchController
from Symbol import Symbol


class GameController:

    def __init__(self):
        self.game_is_over = bool(False)

    def run_tic_tac_toe(self):
        self.ask_player_which_symbol(self)
        while (self.user_cant_get_enough()):
            match = Match(self.player_symbol)
            self.print_instructions(self);
            GameboardDrawer.draw_gameboard(match.grid)
            match_controller = MatchController(match)
            match_controller.start_match()
        else:
            print("Bye.")
            exit()

    def user_cant_get_enough(self):
        print("Do you want to play again? [re][restart] [ex][exit]")
        print(">_")
        user_input = input()
        if user_input == "restart" or user_input == "re":
            return bool(True)
        elif user_input == "exit" or user_input == "ex":
            return bool(False)
        else:
            print("Please, play by the rules. Try again.")
        return bool(False)

    def ask_player_which_symbol(self):
        print("Hello!\nAre you X or O?: [X] [O]\n")
        print(">_")
        user_input = input()
        if self.check_character_for_validity(self,user_input):
            self.save_chosen_character(self, user_input)
        else:
            print("Try again.")
            self.ask_player_which_symbol(self);

    def print_instructions(self):
        print("You are " + self.player_symbol + ". ")
        print("You start.\n")
        print("Enter your field coordinate.")

    def save_chosen_character(self, user_input):
        if (user_input == "X") or (user_input == "x"):
            self.player_symbol = Symbol.X
        elif (user_input == "O") or (user_input == "o"):
            self.player_symbol = Symbol.O

    def check_character_for_validity(user_input):
        return (user_input == "X") or (user_input == "x") or (user_input == "O") or (user_input == "o")

