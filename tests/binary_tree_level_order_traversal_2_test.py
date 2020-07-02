import unittest
from collections import namedtuple

from binary_tree_level_order_traversal_2 import solution, create_tree


class TestBinaryTreelevelOrderTraversal2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Cases = namedtuple("Case", "list_of_nodes, expected")
        cls.testcases = [Cases([3, 9, 20, None, None, 15, 7], [[15, 7], [9, 20], [3]],)]

    def test_solution(self):
        for num, case in enumerate(self.testcases, start=1):
            with self.subTest(f"Case {num}:"):
                tree = create_tree(case.list_of_nodes, len(case.list_of_nodes), 0)
                result = solution(tree)
                self.assertEqual(result, case.expected)


if __name__ == "__main__":
    unittest.main()
