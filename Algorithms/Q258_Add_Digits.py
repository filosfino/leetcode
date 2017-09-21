# -- coding: utf-8 --

class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = 0
        for i in str(num):
            s += int(i)
            s = sum(divmod(s, 10))
        return s

