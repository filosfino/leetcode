# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        current = head
        mark = None
        while current:
            print('looping: %s' % current.val)
            if count == n:
                mark = mark.next if mark else head
                print('marked: %s' % mark.val)
            else:
                count += 1
            current = current.next
        if mark:
            mark.next = mark.next.next
        else:
            return head.next
        return head


