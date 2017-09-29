# -- coding: utf-8 --

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num.is_integer() and num > 1:
            num /= 4
        return num == 1

    def isPowerOfFour(self, num):
        """
        :type n: int
        :rtype: bool
        """
        return num > 0 and num & (num-1) == 0 and (num & 0x55555555 == num)

