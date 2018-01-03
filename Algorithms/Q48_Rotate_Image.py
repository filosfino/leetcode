class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def rotate_single_position(i, j):
            t1, t2, t3, t4 = matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i]
            matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i] = t4, t1, t2, t3

        length = len(matrix)
        for i in range(length//2):
            for j in range(i, length-i-1):
                rotate_single_position(i, j)
