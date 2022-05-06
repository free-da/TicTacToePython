import Field
from Symbol import Symbol


class Grid:
    # private Field[][] fieldMatrix;
    # final int numberOfRows;
    # final int numberOfColumns;

    def __init__(self):
        self.number_of_rows = 3
        self.number_of_columns = self.number_of_rows
        self.field_matrix = [[Field] * self.number_of_columns] * self.number_of_rows
    # for (int i=0; i < numberOfRows; i++) {
    # for (int j=0; j < numberOfColumns; j++) {
    # this.fieldMatrix[i][j] = new Field();

    def set_field_value(self, row_index, column_index, value):
        field = self.field_matrix[row_index][column_index]
        field.set_field_symbol(self, value)

    def get_field_value(self, row_index, colum_index):
        field = self.field_matrix[row_index][colum_index]
        return field.get_value(self);

    def check_if_field_is_empty(self, row_index, column_index):
        return bool(self.get_field_value(row_index, column_index) == Symbol.EMPTY);
