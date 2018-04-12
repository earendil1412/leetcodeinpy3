# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carrying = 0
        result = ListNode(0)
        temp = result
        while l1 is not None or l2 is not None:
            x = 0
            y = 0
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            if l2 is not None:
                y = l2.val
                l2 = l2.next
            num = x + y + carrying
            if num >= 10:
                carrying = 1
                num = num - 10
            else:
                carrying = 0
            temp.next = ListNode(num)
            temp = temp.next
        if carrying > 0:
            temp.next = ListNode(carrying)
        return result.next
