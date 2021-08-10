import unittest
import calc


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 3), 4)
        self.assertEqual(calc.add(1, 5), 6)
        self.assertEqual(calc.add(1, 0), 1)

    def test_subtract(self):
        self.assertEqual(calc.subtract(1, 3), -2)
        self.assertEqual(calc.subtract(1, 0.1), 0.9)
        self.assertEqual(calc.subtract(1, -3), 4)

    def test_multiply(self):
        self.assertEqual(calc.multiply(0, 98), 0)

    def test_divide(self):
        if calc.add(1, 2) != 2:
            self.fail()


if __name__ == '__main__':
    unittest.main()
