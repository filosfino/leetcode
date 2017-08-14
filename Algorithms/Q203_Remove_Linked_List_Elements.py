# -- coding: utf-8 --

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        my_head = ListNode(None)
        my_head.next = head

        current = my_head

        while current.next:
            if current.next.val == val:
                current.next = current.next.next or None
            else:
                current = current.next
        return my_head.next
