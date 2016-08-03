class NumeralDecimalConverter:

    decimal_to_numeral_data = {
        5: 'V',
        1: 'I'
    }

    def __init__(self):
        pass

    #
    # Base method that will evaluate a user input on how to convert it
    # between decimal and roman numerals
    #
    def convert(self, user_input):

        if isinstance(user_input, int):
            return self.decimal_to_numeral_conversion(user_input)
        elif isinstance(user_input, str) and user_input.isdecimal():
            return self.decimal_to_numeral_conversion(int(user_input))

        return False

    #
    # Method that will only do decimal to numeral conversions
    #
    def decimal_to_numeral_conversion(self, decimal_value):

        # Init an output string of numeral characters
        output_string = ''

        # While the value is greater than zero, add an 'I' numeral and
        # decrease the remaining value by 1.
        while decimal_value > 0:
            for dict_decimal, numeral in sorted(self.decimal_to_numeral_data.items(), reverse=True):
                if dict_decimal <= decimal_value:
                    output_string += numeral
                    decimal_value -= dict_decimal
                    break

        # Return the output string
        return output_string
