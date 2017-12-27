# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        h, current = self.swap(current)
        while current:
            _, current = self.swap(current)
        return h

    def swap(self, n1):
        """
        返回 head, n2.next
        :param n1:
        :return:
        """
        if not n1:
            return n1, None
        if n1.next:
            n2 = n1.next
        else:
            return n1, None
        tmp = n2.next
        n2.next = n1
        n1.next = tmp
        if tmp:
            if tmp.next:
                n1.next = tmp.next
        return n2, tmp

