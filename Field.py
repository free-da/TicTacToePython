import Symbol


class Field:
    # private Symbol value;

    def __init__(self, entry):
        if self is not None and entry is None:
            self.value = Symbol.EMPTY;
        elif self is not None and entry is not None:
            self.value = entry

    def get_value(self):
        return self.value

    def set_field_symbol(self, symbol):
        self.value = symbol