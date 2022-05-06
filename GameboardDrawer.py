from Symbol import Symbol


class GameboardDrawer:

    @staticmethod
    def draw_gameboard(grid):
        column_caption_values = GameboardDrawer.get_column_caption_values(grid)
        row_caption_values = GameboardDrawer.get_row_caption_values(grid)
        printable_column_caption = GameboardDrawer.make_beautiful_column_caption(column_caption_values)
        printable_grid = GameboardDrawer.make_printable_grid_rows(row_caption_values, grid);
        inbetween_rows = GameboardDrawer.make_beautiful_row_separator(grid);
        print(printable_column_caption)
        print(inbetween_rows)
        for i in printable_grid:
            print(i)
            print(inbetween_rows)
        print()

    def make_beautiful_row_separator(grid):
        row_separator_builder = "--"
        for i in grid.number_of_columns:
            row_separator_builder += "+---"

        row_separator_builder += "+"
        return row_separator_builder

    def make_printable_grid_rows(row_caption_values, grid):
        printable_grid= ""
        for i in grid.number_of_rows:
            row = row_caption_values.get(i) + " |"
        for j in grid.number_of_columns:
            row += " " + GameboardDrawer.draw_field_type(grid.get_field_value(i, j)) + " |";
            printable_grid += row

        return printable_grid;

    def draw_field_type(field_type):
        if field_type == Symbol.X:
            return "x"
        if field_type == Symbol.O:
            return "O"
        if field_type == Symbol.EMPTY:
            return " "

    def make_beautiful_column_caption(column_caption_values):
        column_caption_builder = ""
        column_caption_builder += "  |"
        for i in column_caption_values:
            column_caption_builder += " " + column_caption_builder[i] + " |"

        return column_caption_builder


    def get_column_caption_values(grid):
        column_caption_helper = ["A", "B", "C", "D", "E", "F"]
        return column_caption_helper[0:grid.number_of_columns-1]

    def get_row_caption_values(grid):
        row_caption_helper = {"1", "2", "3", "4", "5", "6"}
        return row_caption_helper[0:grid.number_of_rows-1]