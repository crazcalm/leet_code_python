"""
Given a binary tree, return the bottom-up level order traversal
of its nodes' value.

- ie, form left to right, level by level from leaf to root.

For example:
    Given binary tree [3, 9, 20, null, null, 15, 7]

           3
          / \
         9  20
           /  \
          15   7

    return its bottom-up level order traversal as:

    [
        [15, 7],
        [9, 20],
        [3],
    ]
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(nodes: List, list_lenght: int, current_index) -> TreeNode:
    if current_index >= list_lenght:
        return TreeNode(val=None)

    val = nodes[current_index]
    left_node_index = (2 * current_index) + 1
    right_node_index = (2 * current_index) + 2

    if val is None:
        return TreeNode(val=None)

    else:
        return TreeNode(
            val=val,
            left=create_tree(nodes, list_lenght, left_node_index),
            right=create_tree(nodes, list_lenght, right_node_index),
        )


def get_tree_height(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        l_height = get_tree_height(root.left)
        r_height = get_tree_height(root.right)

        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1


def get_level_items(root: TreeNode, level: int, answer: List[int]) -> None:
    if root is None:
        return

    if level == 1:
        if root.val is not None:
            answer.append(root.val)
    elif level > 1:
        get_level_items(root.left, level - 1, answer)
        get_level_items(root.right, level - 1, answer)


def solution(root: TreeNode) -> List[List[int]]:
    result = []
    height = get_tree_height(root)

    for level in reversed(range(1, height + 1)):
        tempt = []
        get_level_items(root, level, tempt)

        if tempt:  # Make sure it is not empty
            result.append(tempt)

    return result


if __name__ == "__main__":
    node4 = TreeNode(val=15)
    node5 = TreeNode(val=7)
    node3 = TreeNode(val=20, left=node4, right=node5)
    node2 = TreeNode(val=9)
    node1 = TreeNode(val=3, left=node2, right=node3)

    test = [3, 9, 20, None, None, 15, 7, None, None, None, None, None, None, None, None]
    tree = create_tree(test, len(test), 0)

    print(f"Example answer {solution(node1)}")
    print(f"Example answer that uses my create_tree method {solution(tree)}")
