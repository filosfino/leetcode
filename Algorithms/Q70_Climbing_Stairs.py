class Solution(object):

    cache = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        if Solution.cache.get(n, None) is None:
            Solution.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return Solution.cache[n]
