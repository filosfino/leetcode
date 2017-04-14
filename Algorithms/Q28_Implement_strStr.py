# -- coding: utf-8 --


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        length = len(needle)
        if not length:
            return 0

        if haystack[:length] == needle:
            return 0

        for i in range(len(haystack)-length+1):
            if haystack[i:i+length] == needle:
                return i

        return -1

