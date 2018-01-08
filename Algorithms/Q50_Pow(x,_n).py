# -- coding: utf-8 --

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x, n = 1/x, -n

        def _myPow(x, n):
            if n == 0:
                return 1
            if n & 1:
                return x*_myPow(x*x, n>>1)
            else:
                return _myPow(x*x, n>>1)
        return _myPow(x, n)


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x, n = 1/x, -n
        if n == 0:
            return 1
        factor = 1
        while n > 1:
            if n & 1:
                factor *= x
            x *= x
            n >>= 1
        return factor * x


