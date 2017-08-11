# -- coding: utf-8 --

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        s = ''.join(filter(str.isalnum, s.lower().encode()))
        return s[::-1] == s
