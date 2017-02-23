class Solution(object):
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s, total=0):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return total
        if len(s) == 1 or Solution.mapping[s[0]] >= Solution.mapping[s[1]]:
            return self.romanToInt(s[1:], total + Solution.mapping[s[0]])
        else:
            return self.romanToInt(s[2:], total + Solution.mapping[s[1]] - Solution.mapping[s[0]])
