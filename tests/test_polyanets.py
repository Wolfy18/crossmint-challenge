import unittest

from crossmint_challenge.models import POLYanets


class TestPOLYanets(unittest.TestCase):

    def test_create_polyanets(self):

        poly1 = POLYanets(row=0, column=1)
        poly2 = POLYanets(row=1, column=2)

        self.assertIsInstance(poly1, POLYanets)
        self.assertIsInstance(poly2, POLYanets)

        self.assertEqual(poly2.column, 2)
        self.assertEqual(poly1.row, 0)


if __name__ == "__main__":
    unittest.main()
