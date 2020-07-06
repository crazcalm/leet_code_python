import unittest
from collections import namedtuple

from prison_cells_after_n_days import solution_2


class PrisonCellsAfterNDays(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Case = namedtuple("Case", "cells, days, expected")
        cls.test_cases = [
            Case([0, 1, 0, 1, 1, 0, 0, 1], 7, [0, 0, 1, 1, 0, 0, 0, 0]),
            Case([1, 0, 0, 1, 0, 0, 1, 0], 1000000000, [0, 0, 1, 1, 1, 1, 1, 0]),
        ]

    def solution_setup(self, func):
        for num, case in enumerate(self.test_cases):
            with self.subTest(f"Test {num}:"):
                result = func(case.cells, case.days)
                self.assertEqual(result, case.expected)

    def test_solution(self):
        self.solution_setup(solution_2)


if __name__ == "__main__":
    unittest.main()
