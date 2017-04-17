class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        left = 1
        right = x
        while 1:
            middle = left + (right - left)/2
            if middle > x/middle:
                right = middle - 1
            else:
                if middle + 1 > x/(middle + 1):
                    return middle
                left = middle + 1

