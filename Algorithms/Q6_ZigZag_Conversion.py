# -- coding: utf-8 --


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ret = []
        for i in range(numRows):
            ret.append([])

        if numRows == 1:
            return s

        direction = 1
        row = 0
        for i in s:
            ret[row].append(i)
            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1
            row += direction

        ret_val = []
        for i in range(numRows):
            ret_val.append(''.join(ret[i]))
        return ''.join(ret_val)
