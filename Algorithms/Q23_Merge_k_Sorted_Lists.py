# -- coding: utf-8 --

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        cur = None
        if not all([i for i in lists]):
            lists = [i for i in lists if i]
        while len(lists):
            lists = sorted(lists, key=lambda i: i.val)
            if not head:
                head = lists[0]
                lists[0] = head.next
                cur = head
            else:
                cur.next = lists[0]
                cur = cur.next
                lists[0] = cur.next
            if not all([i for i in lists]):
                lists = [i for i in lists if i]
        return head


from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        cur = dummy = ListNode(None)
        [heappush(pq, (i.val, i)) for i in lists if i]
        while pq:
            cur.next = heappop(pq)[1]
            cur = cur.next
            if cur.next:
                heappush(pq, (cur.next.val, cur.next))
        return dummy.next
