#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# https://leetcode.cn/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (80.22%)
# Likes:    771
# Dislikes: 0
# Total Accepted:    218.1K
# Total Submissions: 271.6K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
#
# 完全二叉树
# 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h
# 层，则该层包含 1~ 2^h 个节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4,5,6]
# 输出：6
#
#
# 示例 2：
#
#
# 输入：root = []
# 输出：0
#
#
# 示例 3：
#
#
# 输入：root = [1]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点的数目范围是[0, 5 * 10^4]
# 0
# 题目数据保证输入的树是 完全二叉树
#
#
#
#
# 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
#
#

# Definition for a binary tree node.
from turtle import left
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def get_half_tree_node_count(self, max_level: int) -> int:
        lvl = 1
        s = 1
        while lvl <= max_level:
            s += 2 ** (lvl - 1)
            lvl += 1
        return s

    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 二分可以快速获取一半的数量
        if not root:
            return 0

        has_children = root.left or root.right
        if not has_children:
            return 1

        cur = root
        tree_height = 0
        while cur.left:
            cur = cur.left
            tree_height += 1

        cur = root.right
        right_tree_height = 0
        while cur and cur.left:
            cur = cur.left
            right_tree_height += 1

        left_tree_full = tree_height == right_tree_height + 1
        if left_tree_full:
            return self.get_half_tree_node_count(tree_height) + self.countNodes(root.right)
        else:
            return self.get_half_tree_node_count(tree_height - 1) + self.countNodes(root.left)


# @lc code=end
