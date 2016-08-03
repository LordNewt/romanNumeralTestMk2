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


    #
    # Decimal to numeral conversion tests
    #

    def test_convert_1_to_numeral_returns_I(self):
        self.assertEqual('I', self.converter.convert(1))

    def test_convert_understands_integers_as_strings(self):
        self.assertEqual('I', self.converter.convert('1'))

    def test_convert_3_to_numeral_returns_III(self):
        self.assertEqual('III', self.converter.convert(3))

    def test_convert_5_to_numeral_returns_V(self):
        self.assertEqual('V', self.converter.convert(5))
