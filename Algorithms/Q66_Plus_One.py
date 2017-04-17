# -- coding: utf-8 --


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(lambda i: int(i), list(str(int(''.join(map(lambda i: str(i), digits))) + 1)))
