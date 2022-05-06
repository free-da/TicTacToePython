class GameController:

    def __init(self):
        self.gameIsOver = bool(False)

    def runTicTacToe(self):
        self.askPlayerWhichSymbol()
        while (user_cant_get_enough()):
            Match
            match = new
            Match(playerSymbol);
            printInstructions();
            GameboardDrawer.drawGameboard(match.grid);
            MatchController
            matchController = new
            MatchController(match);
            matchController.startMatch();

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

    def askPlayerWhichSymbol(self):
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
