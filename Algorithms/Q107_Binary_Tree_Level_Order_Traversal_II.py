# -- coding: utf-8 --

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def get_result(self, level):
        ret = []
        next_level = []
        for item in level:
            if not item:
                continue
            ret.append(item.val)
            if item.left:
                next_level.append(item.left)
            if item.right:
                next_level.append(item.right)
        return ret, next_level

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        result = []
        while level:
            ret, level = self.get_result(level)
            result.append(ret)
        result.reverse()
        return result

