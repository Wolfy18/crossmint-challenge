import unittest

from crossmint_challenge.models import ComETH, POLYanet, SOLoon


class TestModels(unittest.TestCase):

    def test_create_polyanets(self):

        poly1 = POLYanet(row=0, column=1)
        poly2 = POLYanet(row=1, column=2)

        self.assertIsInstance(poly1, POLYanet)
        self.assertIsInstance(poly2, POLYanet)

        self.assertEqual(poly2.column, 2)
        self.assertEqual(poly1.row, 0)

    def test_create_SOLoon(self):

        sol1 = SOLoon(row=1, column=2, color="purple")

        self.assertIsInstance(sol1, SOLoon)
        self.assertEqual(sol1.row, 1)

        # Color is required
        with self.assertRaises(TypeError):
            sol2 = SOLoon(row=0, column=2)

    def test_create_ComETH(self):

        cometh1 = ComETH(row=5, column=2, direction="up")

        self.assertIsInstance(cometh1, ComETH)
        self.assertEqual(cometh1.row, 5)

        # Direction is required
        with self.assertRaises(TypeError):
            cometh2 = ComETH(row=0, column=2)


if __name__ == "__main__":
    unittest.main()
