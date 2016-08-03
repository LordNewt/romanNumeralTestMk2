class NumeralDecimalConverter:

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
            return self.decimal_to_numeral_conversion(user_input)

        return False

    #
    # Method that will only do decimal to numeral conversions
    #
    def decimal_to_numeral_conversion(self, decimal):
        return 'I'
