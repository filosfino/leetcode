#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (64.58%)
# Likes:    632
# Dislikes: 0
# Total Accepted:    155.6K
# Total Submissions: 240.7K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# 给定一个二叉树
#
#
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
#
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
#
#
# 进阶：
#
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
#
#
#
#
# 示例：
#
#
#
#
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next
# 指针连接），'#' 表示每层的末尾。
#
#
#
# 提示：
#
#
# 树中的节点数小于 6000
# -100
#
#
#
#
#
#
#
#


class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# @lc code=start


class Solution:
    def connect(self, root: "Node") -> "Node":
        # 做 root children 的 next 设置
        level_most_left = root
        while level_most_left:
            dummy = Node(0)
            pre = dummy

            cur = level_most_left
            while cur:
                # print(f">> node next start: {cur.val}")
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next

            level_most_left = dummy.next
        return root


# @lc code=end
