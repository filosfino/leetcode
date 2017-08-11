# -- coding: utf-8 --

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def _hasCycle(self, existing_nodes, head):
        if not head:
            return False
        if head in existing_nodes:
            return True
        existing_nodes.add(head)
        return self._hasCycle(existing_nodes, head.next)

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        existing_nodes = set()
        return self._hasCycle(existing_nodes, head)



