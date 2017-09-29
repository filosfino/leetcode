# -- coding: utf-8 --

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n.is_integer() and n > 1:
            n /= 3
        return n == 1

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        return n > 0 and 3 ** int(math.log(2 ** 31, 3)) % n == 0
