from collections import deque

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        q = deque()
        for i, char in enumerate(s):
            if char not in q:
                q.append(char)
            else:
                max_len = max(max_len, len(q))
                while q.popleft() != char:
                    pass
                q.append(char)
        return max(max_len, len(q))
