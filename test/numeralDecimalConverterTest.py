import unittest

from src.numeralDecimalConverter import NumeralDecimalConverter


class NumeralDecimalConverterTest(unittest.TestCase):

    def setUp(self):
        self.converter = NumeralDecimalConverter()

    #
    # Base existence tests
    #

    def test_converter_class_exists(self):
        self.assertIsNotNone(self.converter)

    def test_convert_method_exists(self):
        self.assertRaises(TypeError, self.converter.convert)

    def test_convert_requires_input(self):
        self.assertFalse(self.converter.convert(''))

    def test_convert_rejects_floats(self):
        self.assertFalse(self.converter.convert(1.1))

    def test_convert_rejects_float_as_string(self):
        self.assertFalse(self.converter.convert('1.1'))

    def test_convert_rejects_unknown_numeral(self):
        self.assertFalse(self.converter.convert('MCEVI'))


    #
    # Decimal to numeral conversion tests
    #

    def test_convert_1_to_numeral_returns_I(self):
        self.assertEqual('I', self.converter.convert(1))

    def test_convert_understands_integers_as_strings(self):
        self.assertEqual('I', self.converter.convert('1'))

    def test_convert_can_do_repetitive_numerals(self):
        self.assertEqual('III', self.converter.convert(3))

    def test_convert_recognizes_all_valid_numerals(self):
        self.assertEqual('MDCLXVI', self.converter.convert(1666))

    def test_convert_can_combine_numerals_to_represent_value_decreases(self):
        self.assertEqual('IV', self.converter.convert(4))

    def test_convert_can_handle_multiples_and_value_decreases(self):
        self.assertEqual('MCMLXXXIX', self.converter.convert(1989))


    #
    # Numeral to decimal conversion tests
    #

    def test_convert_I_to_decimal_returns_1(self):
        self.assertEqual(1, self.converter.convert('I'))

    def test_convert_i_to_decimal_returns_1(self):
        self.assertEqual(1, self.converter.convert('i'))

    def test_convert_understands_repetitive_numerals(self):
        self.assertEqual(3, self.converter.convert('III'))

    def test_convert_recognizes_all_numerals(self):
        self.assertEqual(1666, self.converter.convert('MDCLXVI'))

    def test_convert_understands_value_decrese_numerals(self):
        self.assertEqual(4, self.converter.convert('IV'))
