# -- coding: utf-8 --
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build_link_str(self, prefix, val):
        if prefix:
            return '%s->%s' % (prefix, val)
        else:
            return str(val)

    def binaryTreePaths(self, root, prefix=''):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        all_paths = []
        if root is None:
            return all_paths
        if root.left is None and root.right is None:
            all_paths.append(self.build_link_str(prefix, root.val))
            return all_paths
        if root.left:
            all_paths.extend(self.binaryTreePaths(root.left, self.build_link_str(prefix, root.val)))
        if root.right:
            all_paths.extend(self.binaryTreePaths(root.right, self.build_link_str(prefix, root.val)))
        return all_paths
