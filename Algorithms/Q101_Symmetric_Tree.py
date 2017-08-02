# -- coding: utf-8 --

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_sym(L, R):
            if L is None and R is None:
                return True
            elif L and R:
                return L.val == R.val and is_sym(L.left, R.right) and is_sym(L.right, R.left)
            else:
                return False
        return is_sym(root, root)
