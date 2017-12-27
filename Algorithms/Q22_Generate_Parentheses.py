class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        if n == 0:
            return ret
        prefix = '('
        incomplete = 1
        n -= 1
        return self.generate_parenthesis(prefix, n, incomplete)

    def generate_parenthesis(self, prefix, n, incomplete):
        ret = []
        if n:
            ret.extend(self.generate_parenthesis(prefix+'(', n-1, incomplete+1))
        if incomplete:
            ret.extend(self.generate_parenthesis(prefix+')', n, incomplete-1))
        if n == 0 and incomplete == 0:
            ret.append(prefix)
        return ret
