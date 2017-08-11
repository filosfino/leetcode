# -- coding: utf-8 --

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = 1
        ret = 0
        ord_A = ord('A')
        for i in reversed(s):
            ret += base * (ord(i) - ord_A + 1)
            base *= 26
        return ret



