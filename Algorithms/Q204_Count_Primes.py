# -- coding: utf-8 --

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        result = [False] * 2 + [True] * (n - 2)

        for i in range(2, int(n ** 0.5) + 1):
            if result[i]:
                result[i**2:n:i] = [False] * len(result[i**2:n:i])
        return sum(result)

