#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode.cn/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (52.31%)
# Likes:    1510
# Dislikes: 0
# Total Accepted:    504.4K
# Total Submissions: 961K
# Testcase Example:  '[1,2,2,1]'
#
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,2,1]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：head = [1,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 链表中节点数目在范围[1, 10^5] 内
# 0 <= Node.val <= 9
#
#
#
#
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#
#


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

# @lc code=start


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find mid
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 12321
        #   s f
        # 1221x
        #   s f
        b = head
        a = self.reverse(slow)
        while a and b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


# @lc code=end
