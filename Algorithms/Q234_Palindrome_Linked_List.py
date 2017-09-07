# -- coding: utf-8 --

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        value_list = []
        current = head
        while current:
            value_list.append(current.val)
            current = current.next
        return self.isPalindromeList(value_list)

    def isPalindromeList(self, value_list):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = len(value_list) // 2
        if length <= 0:
            return True
        return value_list[:length] == value_list[-length:][::-1]
