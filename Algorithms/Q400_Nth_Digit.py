# -- coding: utf-8 --

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 0
        tmp = 0
        max_digits = 0
        while max_digits + tmp < n:
            max_digits += tmp
            digit += 1
            tmp = digit*(9*10**(digit-1))
        remaining_digits = n - max_digits - 1
        return int(str(10**(digit-1) + remaining_digits//digit)[remaining_digits%digit])

