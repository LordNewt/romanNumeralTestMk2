from src.numeralDecimalUtils import NumeralDecimalUtils


class NumeralDecimalConverter:

    def __init__(self):
        self.numeralDecimalUtils = NumeralDecimalUtils()

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
        # Keep track of the previous numeral value which is useful for
        # "reduce by" calculations
        previous_value = 0
        # Keep track of how many of the same numeral have repeated
        repeat_data = {'previous_numeral': '', 'numeral_repeat_count': 0, 'too_repetitive': False}

        # Loop through each numeral in the list
        while position < len(numeral_list):
            current_numeral = numeral_list[position]

            # Check if we've hit an illegally repetitive numeral. First,
            # is it the same numeral
            repeat_data = self.numeralDecimalUtils.is_numeral_too_repetitive(current_numeral, repeat_data)
            if repeat_data['too_repetitive']:
                return False

            # Get the best value for the numeral
            result = self.numeralDecimalUtils.get_value(current_numeral)
            if not result:
                return False

            # If the previous numeral value is less than the current numeral,
            # it indicates that the previous should have been subtracted, not
            # added.
            if 0 < previous_value < result:
                # First, make sure the previous value was a legal subtraction
                if not self.numeralDecimalUtils.is_legal_subtraction(current_numeral, previous_value):
                    return False
                # The previous value was added instead of subtracted. To deal
                # with this, subtract 2x the previous value before adding the
                # new value.
                output_value -= (2 * previous_value)

            # Add the current numeral's value, and set it as the "previous"
            # value for the next iteration
            output_value += result
            previous_value = result

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
            numeral_data = self.numeralDecimalUtils.get_best_numeral(decimal_value)
            output_string += numeral_data['numeral']
            decimal_value -= numeral_data['value']

        # Return the output string
        return output_string
