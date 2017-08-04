# -- coding: utf-8 --

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, 0)]
        while stack:
            item, current_sum = stack.pop()
            if not item.left and not item.right:
                if current_sum + item.val == sum:
                    return True
                continue
            if item.left:
                stack.append((item.left, current_sum + item.val))
            if item.right:
                stack.append((item.right, current_sum + item.val))
        return False
