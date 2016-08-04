class NumeralDecimalUtils:

    # Decimal/Numeral conversion data dictionary
    numeral_decimal_data = [
        {'numeral': 'M', 'value': 1000, 'reduced_by': 100, 'max_repeats': 3},
        {'numeral': 'D', 'value': 500, 'reduced_by': 100, 'max_repeats': 1},
        {'numeral': 'C', 'value': 100, 'reduced_by': 10, 'max_repeats': 3},
        {'numeral': 'L', 'value': 50, 'reduced_by': 10, 'max_repeats': 1},
        {'numeral': 'X', 'value': 10, 'reduced_by': 1, 'max_repeats': 3},
        {'numeral': 'V', 'value': 5, 'reduced_by': 1, 'max_repeats': 1},
        {'numeral': 'I', 'value': 1, 'reduced_by': 0, 'max_repeats': 3}
    ]

    #
    # Returns the numeral for a decimal value
    #
    def get_numeral(self, decimal_value):
        for conversion_data in self.numeral_decimal_data:
            if conversion_data['value'] == decimal_value:
                return conversion_data['numeral']
        return None

    #
    # Returns the numeral data dictionary for a given numeral
    #
    def get_numeral_data(self, numeral):
        for conversion_data in self.numeral_decimal_data:
            if conversion_data['numeral'] == numeral:
                return conversion_data
        return {}

    #
    # Returns the decimal value of the given numeral
    #
    def get_value(self, numeral):
        numeral_data = self.get_numeral_data(numeral)
        if not numeral_data:
            return None
        return numeral_data['value']

    #
    def is_numeral_too_repetitive(self, numeral, current_repeat_count):
        numeral_data = self.get_numeral_data(numeral)
        return numeral_data['max_repeats'] <= current_repeat_count


    #
    # Returns the best numeral (or numeral combo) for a given decimal value
    # as well as the value of that numeral
    #
    def get_best_numeral(self, decimal_value):

        best_numeral = ''
        numeral_value = 0

        # Go through each numeral entry, seeking out the highest value option
        for conversion_data in self.numeral_decimal_data:

            # If the current numeral has a value less than or equal to
            # the remaining decimal_value, add that numeral to the output
            # and reduce by the value of the numeral
            if numeral_value < conversion_data['value'] <= decimal_value:
                best_numeral = conversion_data['numeral']
                numeral_value = conversion_data['value']
                break

            # If the current numeral minus its 'reduced by' value is less
            # than or equal to the remaining decimal_value, add the numeral
            # combo to the output and reduce by the value of the difference
            # of the two numerals
            elif numeral_value < (conversion_data['value'] - conversion_data['reduced_by']) <= decimal_value:
                best_numeral = self.get_numeral(conversion_data['reduced_by']) + conversion_data['numeral']
                numeral_value = (conversion_data['value'] - conversion_data['reduced_by'])
                break

        # Return the "best fit" result
        return {'numeral': best_numeral, 'value': numeral_value}
