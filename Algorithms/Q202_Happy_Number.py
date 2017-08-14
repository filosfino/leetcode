# -- coding: utf-8 --

class Solution(object):
    def square_sum(self, n):
        return sum(map(lambda i: int(i)**2, str(n)))

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hash_set = {}
        while n not in hash_set:
            result = self.square_sum(n)
            hash_set[n] = result
            n = result
        return n == 1
