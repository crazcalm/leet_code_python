import unittest
from collections import namedtuple

from add_two_numbers import ListNode, Solution


class TestAddTwoNumbers(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        TestCaseData = namedtuple("cases", "list_node_1, list_node_2 , expected")
        cls.test_cases = [
            TestCaseData(
                ListNode(2, ListNode(4, ListNode(3))),
                ListNode(5, ListNode(6, ListNode(4))),
                ListNode(7, ListNode(0, ListNode(8))),
            ),
        ]

    def test_two_sum(self) -> None:
        for index, test_case in enumerate(self.test_cases, start=1):
            with self.subTest(msg=f"Test case number {index}"):
                result = Solution().add_two_numbers(
                    test_case.list_node_1, test_case.list_node_2
                )
                expected = test_case.expected

                self.assertEqual(result, expected)

    def test_get_num(self):
        test_case = ListNode(2, ListNode(4, ListNode(3)))
        result = Solution().get_number(test_case)

        self.assertEqual("342", result)

    def test_make_list_node(self):
        test_case = "243"
        result = Solution().make_list_node(test_case)
        expected = ListNode(2, ListNode(4, ListNode(3)))

        self.assertEqual(result, expected)

    def test__eq__(self):
        Case = namedtuple("data", "l1, l2, expected")
        cases = [
            Case(ListNode(0), ListNode(0), True),
            Case(ListNode(0), ListNode(1), False),
            Case(ListNode(0, ListNode(1)), ListNode(0, ListNode(1)), True),
            Case(ListNode(0, ListNode(1)), ListNode(0), False),
            Case(ListNode(0, ListNode(1)), ListNode(0, ListNode(1)), True),
            Case(ListNode(0), ListNode(0, ListNode(1)), False),
        ]

        for num, case in enumerate(cases, start=1):
            with self.subTest(msg=f"Case num {num}"):
                result = case.l1 == case.l2
                self.assertEqual(result, case.expected)


if "__main__" == __name__:
    unittest.main()
