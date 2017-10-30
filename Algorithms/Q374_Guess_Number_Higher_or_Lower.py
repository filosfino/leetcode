# -- coding: utf-8 --

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self._guessNumber(1, n)

    def _guessNumber(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if y - x < 2:
            result = guess(x)
            if result == 0:
                return x
            else:
                return y
        else:
            tmp = (x+y)//2
            result = guess(tmp)
            if result == 1:
                return self._guessNumber(tmp+1, y)
            elif result == 0:
                return tmp
            else:
                return self._guessNumber(x, tmp-1)
