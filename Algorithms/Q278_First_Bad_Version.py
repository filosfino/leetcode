# -- coding: utf-8 --
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n, start=1):
        """
        :type n: int
        :rtype: int
        """
        if n - start <= 1:
            if isBadVersion(start):
                return start
            else:
                return n

        middle_version = (n+start)//2
        if isBadVersion(middle_version):
            return self.firstBadVersion(middle_version)
        else:
            return self.firstBadVersion(n, middle_version)

