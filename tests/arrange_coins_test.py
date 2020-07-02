import unittest
from collections import namedtuple

from arranging_coins import arrange_coins


class TestArrangeCoins(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Case = namedtuple("Case", "n, expected")
        cls.testcase = [
            Case(5, 2),
            Case(8, 3),
        ]

    def test_arrange_coins(self):
        for num, case in enumerate(self.testcase, start=1):
            with self.subTest(f"Case number {num}"):
                result = arrange_coins(case.n)
                self.assertEqual(result, case.expected)


if __name__ == "__main__":
    unittest.main()
