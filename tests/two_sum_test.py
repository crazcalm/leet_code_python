import unittest
from collections import namedtuple

from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        TestCaseData = namedtuple("cases", "list, target, expected")
        cls.test_cases = [
            TestCaseData([2, 7, 11, 15], 9, [0, 1]),
            TestCaseData([3, 2, 4], 6, [1, 2]),
        ]

    def test_two_sum(self) -> None:
        for index, test_case in enumerate(self.test_cases, start=1):
            with self.subTest(msg=f"Test case number {index}"):
                result = two_sum(test_case.list, test_case.target)

                self.assertEqual(result, test_case.expected)


if "__main__" == __name__:
    unittest.main()
