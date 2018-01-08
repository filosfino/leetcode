# -- coding: utf-8 --

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m:
            n = len(matrix[0])
        else:
            n = 0
        if not m or not n:
            return []

        def add_circle(ret, nth_circle):
            # print(ret, nth_circle, m, n)
            for i in range(nth_circle, n-nth_circle-1):
                ret.append(matrix[nth_circle][i])
            for i in range(nth_circle, m-nth_circle-1):
                ret.append(matrix[i][n-1-nth_circle])
            for i in range(n-nth_circle-1, nth_circle, -1):
                ret.append(matrix[m-1-nth_circle][i])
            for i in range(m-nth_circle-1, nth_circle, -1):
                ret.append(matrix[i][nth_circle])

        ret = []
        big, small, way = (m,n,'v') if m >=n else (n,m, 'h')
        for i in range(0, small//2):
            add_circle(ret, i)
        if small%2 == 1:
            nth_circle = small//2
            if way=='v':
                for i in range(nth_circle, m-nth_circle):
                    ret.append(matrix[i][n-1-nth_circle])
            else:
                for i in range(nth_circle, n-nth_circle):
                    ret.append(matrix[nth_circle][i])
        return ret
