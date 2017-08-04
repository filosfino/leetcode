# -- coding: utf-8 --

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row_list = [[1], [1, 1]]
        if rowIndex <= 1:
            return row_list[rowIndex]

        current_row_index = 2
        while current_row_index <= rowIndex:
            current_row = [1]
            for i in xrange(current_row_index-1):
                current_row.append(row_list[1][i] + row_list[1][i+1])
            current_row.append(1)
            current_row_index += 1
            row_list[0] = row_list[1]
            row_list[1] = current_row
        return row_list[1]
