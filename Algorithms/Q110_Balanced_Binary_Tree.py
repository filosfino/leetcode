# -- coding: utf-8 --

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_height(self, root):
        if not root:
            return 0
        if root.left or root.right:
            return max(self.get_height(root.left), self.get_height(root.right)) + 1
        else:
            return 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        return abs(self.get_height(root.left) - self.get_height(root.right)) <= 1


