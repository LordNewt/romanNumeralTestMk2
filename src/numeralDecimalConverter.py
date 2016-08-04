class NumeralDecimalConverter:

    # Decimal to numeral conversion data dictionary
    decimal_to_numeral_data = {
        1000: {'numeral': 'M', 'reduced_by': 100},
        500: {'numeral': 'D', 'reduced_by': 100},
        100: {'numeral': 'C', 'reduced_by': 10},
        50: {'numeral': 'L', 'reduced_by': 10},
        10: {'numeral': 'X', 'reduced_by': 1},
        5: {'numeral': 'V', 'reduced_by': 1},
        1: {'numeral': 'I', 'reduced_by': 0}
    }

    def __init__(self):
        pass

    #
    # Base method that will evaluate a user input on how to convert it
    # between decimal and roman numerals
    #
    def convert(self, user_input):

        # Empty input returns false
        if not user_input:
            return False

        # Check if a decimal was passed in to convert to a numeral
        if isinstance(user_input, int):
            return self.decimal_to_numeral_conversion(user_input)
        elif isinstance(user_input, str) and user_input.isdecimal():
            return self.decimal_to_numeral_conversion(int(user_input))

        # Check if a numeral string was passed in to convert to a decimal
        if isinstance(user_input, str) and '.' not in user_input:
            return 1

        # No match means it was invalid, return false
        return False

    #
    # Method that will only do decimal to numeral conversions
    #
    def decimal_to_numeral_conversion(self, decimal_value):

        # Init an output string of numeral characters
        output_string = ''

        # Loop through this section, reducing the remaining decimal_value
        # until it reaches zero
        while decimal_value > 0:

            # Go through each numeral value from highest to lowest to see if
            # that numeral can be added to the output
            for dict_decimal, decimal_data in sorted(self.decimal_to_numeral_data.items(), reverse=True):

                # If the current numeral has a value less than or equal to
                # the remaining decimal_value, add that numeral to the output
                # and reduce by the value of the numeral
                if dict_decimal <= decimal_value:
                    output_string += decimal_data['numeral']
                    decimal_value -= dict_decimal
                    break

                # If the current numeral minus its 'reduced by' value is less
                # than or equal to the remaining decimal_value, add the numeral
                # combo to the output and reduce by the value of the difference
                # of the two numerals
                elif (dict_decimal - decimal_data['reduced_by']) <= decimal_value:
                    output_string += self.decimal_to_numeral_data[decimal_data['reduced_by']]['numeral'] + \
                                     decimal_data['numeral']
                    decimal_value -= (dict_decimal - decimal_data['reduced_by'])
                    break

        # Return the output string
        return output_string
