# -- coding: utf-8 --

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for current_row_index in xrange(numRows):
            if current_row_index <= 1:
                ret.append([1] * (current_row_index + 1))
                continue
            else:
                current_row = [1]
                previous_row = ret[current_row_index-1]
                for index in xrange(current_row_index-1):
                    current_row.append(previous_row[index] + previous_row[index+1])
                current_row.append(1)
            ret.append(current_row)
        return ret



