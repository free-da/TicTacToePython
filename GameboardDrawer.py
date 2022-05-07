from Symbol import Symbol


def draw_gameboard(grid):
    column_caption_values = get_column_caption_values(grid)
    row_caption_values = get_row_caption_values(grid)
    printable_column_caption = make_beautiful_column_caption(column_caption_values)
    printable_grid = make_printable_grid_rows(row_caption_values, grid)
    inbetween_rows = make_beautiful_row_separator(grid)
    print(printable_column_caption)
    print(inbetween_rows)
    for i in printable_grid:
        print(i)
        print(inbetween_rows)
    print()


def make_beautiful_row_separator(grid):
    row_separator_builder = "--"
    for i in range(grid.number_of_columns):
        row_separator_builder += "+---"

    row_separator_builder += "+--"
    return row_separator_builder


def make_printable_grid_rows(row_caption_values, grid):
    printable_grid = []
    for i in range(0, grid.number_of_rows):
        row = row_caption_values[i] + " |"
        for j in range(0, grid.number_of_columns):
            row += " " + draw_field_type(grid.get_field_value(i, j)) + " |"
        printable_grid.append(row)

    return printable_grid


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
        column_caption_builder += " " + i + " |"

    return column_caption_builder


def get_column_caption_values(grid):
    column_caption_helper = ["A", "B", "C", "D", "E", "F"]
    return column_caption_helper[0:grid.number_of_columns]


def get_row_caption_values(grid):
    row_caption_helper = ["1", "2", "3", "4", "5", "6"]
    return row_caption_helper[0:grid.number_of_rows]
