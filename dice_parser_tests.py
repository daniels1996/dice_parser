from dice_parser import get_dice_format
import unittest

class TestDiceParser(unittest.TestCase):

    def test_providenegativedicequantity(self):
        actual = get_dice_format(-10, 6, False)
        expected = "Please use positive and whole numbers only."
        self.assertEqual(actual, expected)

    def test_provide_negative_dice_sides(self):
       actual = get_dice_format(10, -6, False)
       expected = "Please use positive and whole numbers only."
       self.assertEqual(actual, expected)

    def test_provide_decimal_dice_quantity(self):
        actual = get_dice_format(10.5, 6, False)
        expected = "Please use positive and whole numbers only."
        self.assertEqual(actual, expected)

    def test_provide_decimal_dice_sides(self):
        actual = get_dice_format(10, 6.5, False)
        expected = "Please use positive and whole numbers only."
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()