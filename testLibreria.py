import unittest
import Libreria
import math


class PruebaLab(unittest.TestCase):

    def test_SumModulos(self):
        y = [(-3, -1), (0, -2), (0, 1), (2, 0)]
        x = 2
        self.assertEqual(Libreria.SumModulos(y, x), 0.05263157894736842)

    def test_AmplitudTrans(self):
        y = [(2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1)]
        y2 = [(-1, -4), (2, -3), (-7, 6), (-1, 1), (-5, -3), (5, 0), (5, 8), (4, -4), (8, -7), (2, -7)]
        self.assertEqual(Libreria.AmplitudTrans(y, y2), (-0.00014085829655366726, -0.0008921025448398911))



if __name__ == "__main__":
    unittest.main()
