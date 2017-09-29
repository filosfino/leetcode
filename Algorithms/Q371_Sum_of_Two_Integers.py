# -- coding: utf-8 --

MASK = 0xffffffff
MAX = 0x7fffffff


# 大于 0x800000000 的时候应解读为负数，通过 ~(x ^ MASK) 来转化
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            a, b = (a ^ b)&MASK, ((a & b) << 1)&MASK
        return a if a <= MAX else ~(a ^ MASK)
