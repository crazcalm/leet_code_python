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

                current_node = expected
                current_result_node = result
                while current_node:
                    self.assertEqual(current_node.val, current_result_node.val)
                    current_node = current_node.next
                    current_result_node = current_result_node.next

    def test_get_num(self):
        test_case = ListNode(2, ListNode(4, ListNode(3)))
        result = Solution().get_number(test_case)

        self.assertEqual("342", result)

    def test_make_list_node(self):
        test_case = "243"
        result = Solution().make_list_node(test_case)
        expected = ListNode(2, ListNode(4, ListNode(3)))

        current_node = expected
        current_result_node = result
        while current_node:
            self.assertEqual(current_node.val, current_result_node.val)
            current_node = current_node.next
            current_result_node = current_result_node.next


if "__main__" == __name__:
    unittest.main()
