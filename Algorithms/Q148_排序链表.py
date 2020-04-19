#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (64.97%)
# Likes:    494
# Dislikes: 0
# Total Accepted:    54.5K
# Total Submissions: 83.9K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # print(f'sortList: {self.print(head)}')
        l = self.split_chain(head)
        # print(f'splited result:\n{self.print(l[0])}\n{self.print(l[1])}')
        if not l[0]:
            return None
        elif not l[1]:
            ret = l[0]
        else:
            ret = self.merge_sorted(self.sortList(l[0]), self.sortList(l[1]))
        # print(f'sortListReturn: {self.print(ret)}\n')
        return ret

    def merge_sorted(self, first: ListNode, second: ListNode):
        # print(f'merge_sorted first: {self.print(first)}')
        # print(f'merge_sorted second: {self.print(second)}')
        dummy = ListNode(-1)
        cur = dummy
        while first and second:
            if first.val <= second.val:
                cur.next = first
                first = first.next
            else:
                cur.next = second
                second = second.next
            cur = cur.next
        if first:
            cur.next = first
        elif second:
            cur.next = second
        else:
            cur.next = None
        return dummy.next

    def split_chain(self, head: ListNode):
        # print(f'split_chain: {self.print(head)}')
        if not head:
            return [None, None]
        if head.next == None:
            return [head, None]
        if head.next.next == None:
            new_start = head.next
            head.next = None
            return [head, new_start]
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        new_start = slow.next
        slow.next = None
        return [head, new_start]

    # def print(self, head: ListNode):
    #     vals = []
    #     while head:
    #         vals.append(str(head.val))
    #         head = head.next
    #     return '->'.join(vals)


# @lc code=end
