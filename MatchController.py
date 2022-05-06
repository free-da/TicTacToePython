from random import random

from GameboardDrawer import GameboardDrawer
from WinChecker import WinChecker


class MatchController:
    # private Match match;
    # private Random randomizerForBotMoves = new Random();

    def __init__(self, match):
        self.match = match

    def start_match(self):
        self.start_game_loop(self)
        self.announce_end_of_game(self)
        self.announce_winner(self)

    def start_game_loop(self):
        while self.is_game_over() == bool(False):
            self.next_move(self)

    def is_game_over(self):
        if self.someone_won(self):
            self.match.is_game_over = bool(True)
        if self.match.number_of_moves == (self.match.grid.number_of_columns * self.match.grid.number_of_rows):
            self.match.is_game_over = bool(True)
            self.someone_won()
        return self.match.is_game_over

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
            self.player_makes_next_move(self)
        else:
            self.bot_makes_next_move(self)
        self.match.number_of_moves += 1
        GameboardDrawer.drawGameboard(self.match.grid);

    def bot_makes_next_move(self):
        row_index = random.randrange(self.match.grid.numberOfRows)
        column_index = random.randrange(self.match.grid.numberOfColumns)
        if self.match.grid.check_if_field_is_empty(row_index, column_index):
            self.match.grid.setFieldValue(row_index, column_index, self.match.bot_symbol);
            self.match.players_turn = bool(True)
        else:
            self.bot_makes_next_move()

    def player_makes_next_move(self):
        {
        BufferedReader
        bufferedReader = new
        BufferedReader(new
        InputStreamReader(System. in));
        String
        input;
        try {
        System.out.print(">_");
        input = bufferedReader.readLine();
        if (coordinateInputIsValid(input)) {
        match.grid.setFieldValue(findRowIndex(input), findColumnIndex(input), match.playerSymbol);
        } else {
        System.out.println("Please, play by the rules. Try again.");
        playerMakesNextMove();
        }
        } catch(IOException e) {
        System.out.println("Error. Try again.");
        playerMakesNextMove();
        }
        match.playersTurn = false;
        }

    def announce_winner(self):
        {
        if (match.gameIsOver & & someoneWon()) {
        if (match.winner.equals("player")) {
        System.out.println("You won.");
        } else if (match.winner.equals("bot")) {
        System.out.println("You lost. The machine is superior.");
        }
        } else {
        System.out.println("Tied. Everybody loses.");
        }

        }

    def announce_end_of_game(self):
    {
    System.out.println("Game is over.");
    }

    def find_column_index(self, input):
        char
        secondLetter = input.charAt(1);
        String
        coordinatesHelperColumns = "ABCDEFG";
        coordinatesHelperColumns = coordinatesHelperColumns.substring(0, match.grid.numberOfColumns);
        return coordinatesHelperColumns.indexOf(Character.toString(secondLetter).toUpperCase());
        }

    def findRowIndex(self, input):
        char
        firstLetter = input.charAt(0);
        String
        coordinatesHelperRows = "123456";
        coordinatesHelperRows = coordinatesHelperRows.substring(0, match.grid.numberOfRows);
        return coordinatesHelperRows.indexOf(Character.toString(firstLetter).toUpperCase());
        }

    def coordinate_input_is_valid(self, input):
        if (input.length() == 2) {
        int columnIndex = findColumnIndex(input);
        int rowIndex = findRowIndex(input);
        return !(column_index < 0 | | row_index < 0 | | !match.grid.checkIfFieldIsEmpty(rowIndex, columnIndex));
        }
        return false;