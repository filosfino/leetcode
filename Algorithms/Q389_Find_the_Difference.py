# encoding: utf-8
import string


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for l in string.ascii_lowercase:
            if s.count(l) != t.count(l):
                return l
