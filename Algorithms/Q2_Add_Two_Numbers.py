# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def node_add(l1, l2, carry):
    v1 = l1.val if hasattr(l1, 'val') else 0
    v2 = l2.val if hasattr(l2, 'val') else 0
    carry, s = divmod(v1 + v2 + carry, 10)
    return carry, ListNode(s)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node_1 = l1
        node_2 = l2
        ret = ListNode(None)
        node_ret_cur = ret
        carry = 0
        while hasattr(node_1, 'val') or hasattr(node_2, 'val') or carry:
            carry, node_ret_cur.next = node_add(node_1, node_2, carry)
            node_ret_cur = node_ret_cur.next
            node_1 = getattr(node_1, 'next', None)
            node_2 = getattr(node_2, 'next', None)
        r = []
        r_cur = ret
        while r_cur.next:
            r.append(r_cur.next.val)
            r_cur = r_cur.next
        return r
