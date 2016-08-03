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
        self.assertIsNotNone(self.converter.convert(''))
