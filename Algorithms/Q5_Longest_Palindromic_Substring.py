#!/usr/bin/env python
# -- coding: utf-8 --


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        total = 0
        while 1:
            for head in xrange(total+1):
                substring = s[head:-total+head or None]
                if substring == substring[::-1]:
                    return substring
            total += 1

