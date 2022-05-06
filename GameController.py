from GameboardDrawer import GameboardDrawer
from Match import Match


class GameController:

    def __init__(self):
        self.game_is_over = bool(False)

    def run_tic_tac_toe(self):
        self.ask_player_which_symbol()
        while (self.user_cant_get_enough()):
            match = Match(self.player_symbol)
            self.print_instructions();
            GameboardDrawer.draw_gameboard(match.grid)
            matchController = MatchController(match);
            matchController.start_match();

        else:
            print("Bye.")
            exit()

def user_cant_get_enough(self):
{
System.out.println("Do you want to play again? [re][restart] [ex][exit]");
BufferedReader
bufferedReader = new
BufferedReader(new
InputStreamReader(System. in));
try {
System.out.print(">_");
String input = bufferedReader.readLine();
if (input.equals("restart") | | input.equals("re")) {
return true;
} else if (input.equals("exit") | | input.equals("ex")) {
return false;
} else {
System.out.println("Please, play by the rules. Try again.");
}
} catch(IOException
e) {
    System.out.println("Error. Try again.");
userCantGetEnough();
}
return false;
}

    def ask_player_which_symbol(self):
BufferedReader
bufferedReader = new
BufferedReader(new
InputStreamReader(System. in));
System.out.print("Hello!\nAre you X or O?: [X] [O]\n");
try {
System.out.print(">_");
String input = bufferedReader.readLine();
if (checkCharacterForValidity(input)) {
saveChosenCharacter(input);
} else {
System.out.println("Try again.");
askPlayerWhichSymbol();
}
} catch(IOException e) {
System.out.println("Error. Try again.");
askPlayerWhichSymbol();
}
}

private
void
printInstructions()
{
System.out.print("You are " + playerSymbol + ". ");
System.out.print("You start.\n");
System.out.println("Enter your field coordinate.");
}

private
void
saveChosenCharacter(String
input) {
if ((input.equals("X")) | | (input.equals("x"))) {
playerSymbol = Symbol.X;
} else if ((input.equals("O")) | | (input.equals("o"))) {
playerSymbol = Symbol.O;
}
}

private
boolean
checkCharacterForValidity(String
input) {
return ((input.equals("X")) | | (input.equals("x")) | | (input.equals("O")) | | (input.equals("o")));
}
}
