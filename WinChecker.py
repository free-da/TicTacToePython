from Symbol import Symbol


class WinChecker:

    @staticmethod
    def check_if_either_won(symbol, grid):
        if symbol == Symbol.X or symbol == Symbol.O:

            ###check for Rows
            for row_index in grid.number_of_rows:
                row_check_counter = WinChecker.number_of_checks_in_row(symbol, grid, row_index);
                if (row_check_counter == 3):
                    return bool(True)
            ###check for columns
            for column_index in grid.number_of_columns:
                column_check_counter = WinChecker.number_of_checks_in_column(symbol, grid, column_index);
                if column_check_counter == 3:
                    return bool(True)
            ###check for diagonal
            WinChecker.check_for_diagonal_win(symbol, grid)
            return bool(False)

    def check_for_diagonal_win(symbol, grid):
        ### only works for 3x3 grid
        if grid.get_field_value(1, 1) == symbol:
            if grid.get_field_value(0, 0) == symbol and grid.get_field_value(2, 2) == symbol:
                return bool(True)
            if grid.get_field_value(0, 2) == symbol and grid.get_field_value(2, 0) == symbol:
                return bool(True)
        return bool(False)

    def number_of_checks_in_column(symbol, grid, column_index):
        counter = 0
        for row_index in grid.numberOfRows:
            if grid.get_field_value(row_index, column_index) == symbol:
                counter += 1
        return counter


    def number_of_checks_in_row(symbol, grid, row_index):
        counter = 0
        for column_index in grid.number_of_columns:
            if grid.get_field_value(row_index, column_index) == symbol:
                counter += 1
        return counter