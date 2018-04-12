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
        addition = 0
        result = ListNode(0)
        temp = result
        while l1 is not None or l2 is not None:
            if temp is None:
                temp = ListNode(0)
            x = 0
            y = 0
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            if l2 is not None:
                y = l2.val
                l2 = l2.next
            num = x + y + addition
            if num >= 10:
                addition = 1
            else:
                addition = 0
            temp.next = ListNode(num % 10)
            temp = temp.next
        if addition > 0:
            temp.next = ListNode(addition)
        return result.next
