# -- coding: utf-8 --
import string

class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = []
        while 1:
            n, tail = divmod(n-1, 26)
            ret.append(string.ascii_uppercase[tail])
            if not n:
                break
        return ''.join(ret[::-1])

