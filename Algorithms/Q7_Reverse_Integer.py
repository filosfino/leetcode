# -- coding: utf-8 --


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_positive_vale = 2**31-1
        min_negative_vale = -2**31
        char_list = list(str(x))
        if char_list[0] == '-':
            ret = ['-']
            ret.extend(char_list[-1:0:-1])
        else:
            ret = char_list[::-1]
        ret = int(''.join(ret))
        if not (min_negative_vale <= ret <= max_positive_vale):
            return 0
        return ret
