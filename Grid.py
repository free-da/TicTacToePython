from Field import Field
from Symbol import Symbol


class Grid:
    # private Field[][] fieldMatrix;
    # final int numberOfRows;
    # final int numberOfColumns;

    def __init__(self):
        self.number_of_rows = 3
        self.number_of_columns = self.number_of_rows
        self.field_matrix = []
        for i in range(self.number_of_rows):
            row = []
            for j in range(self.number_of_columns):
                row.append(Field())
            self.field_matrix.append(row)

    def set_field_value(self, row_index, column_index, value):
        field = self.field_matrix[row_index][column_index]
        field.set_field_symbol(value)

    def get_field_value(self, row_index, colum_index):
        field = self.field_matrix[row_index][colum_index]
        return field.get_value()

    def check_if_field_is_empty(self, row_index, column_index):
        return bool(self.get_field_value(row_index, column_index) == Symbol.EMPTY)
