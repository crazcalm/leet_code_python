"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in
reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        result = True
        current_node = self
        current_other_node = other

        while current_node is not None:
            if current_other_node is None:
                result = False
                break

            elif current_node.val != current_other_node.val:
                result = False
                break

            current_node = current_node.next
            current_other_node = current_other_node.next

        if current_node is None:
            if current_other_node is not None:
                result = False

        return result


class Solution:
    def get_number(self, list_node: ListNode) -> str:
        if list_node.next is None:
            return list_node.val
        else:
            return str(self.get_number(list_node.next)) + str(list_node.val)

    def make_list_node(self, num):
        if len(num) == 0:
            return None
        else:
            return ListNode(val=int(num[0]), next=self.make_list_node(num[1:]))

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_1 = self.get_number(l1)
        num_2 = self.get_number(l2)

        result = int(num_1) + int(num_2)
        result = str(result)
        result = result[::-1]

        return self.make_list_node(result)
