import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        assert add(1, 2) == 3
        assert add(4, 5) == 9
        assert add(7, 6) == 13

    def test_subtract(self):  # 3 assertions
        assert add(1, 2) == 3
        assert add(4, 5) == 9
        assert add(7, 6) == 13

    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 3), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(0, 3), 0)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 7)

    def test_logarithm(self):  # 3 assertions
        assert log(2, 4) == 2
        assert log(3, 9) == 2
        assert log(3, 27) == 3

    def test_log_invalid_base(self):  # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(0, 7)

    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):  # 3 assertions
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-4)

    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
