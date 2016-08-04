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

    # Numeral to decimal value data dictionary
    numeral_to_decimal_data = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
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
            return self.numeral_to_decimal_conversion(user_input.upper())

        # No match means it was invalid, return false
        return False

    #
    # Method that will do the numeral to decimal conversions
    #
    def numeral_to_decimal_conversion(self, numeral_value):
        # Break numeral string into list of characters
        numeral_list = list(numeral_value)
        # Set position in the list to the beginning
        position = 0
        # Set output value to zero
        output_value = 0

        # Loop through each numeral in the list
        while position < len(numeral_list):
            if numeral_list[position] not in self.numeral_to_decimal_data:
                return False
            # Add the value of the current numeral to the output value
            output_value += self.numeral_to_decimal_data[numeral_list[position]]
            # Move to the next position in the list
            position += 1

        # Return the resulting value
        return output_value

    #
    # Method that will do the decimal to numeral conversions
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
