class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        length = len(board)
        def row_check(x):
            tmp = set()
            for i in range(length):
                if board[x][i] != '.':
                    if board[x][i] in tmp:
                        return False
                    else:
                        tmp.add(board[x][i])
            return True

        def column_check(x):
            tmp = set()
            for i in range(length):
                if board[i][x] != '.':
                    if board[i][x] in tmp:
                        return False
                    else:
                        tmp.add(board[i][x])
            return True

        def box_check(x):
            row_start = x//3*3
            column_start = x%3*3

            tmp = set()
            for i in range(row_start, row_start+3):
                for j in range(column_start, column_start+3):
                    if board[i][j] != '.':
                        if board[i][j] in tmp:
                            return False
                        else:
                            tmp.add(board[i][j])
            return True

        for i in range(length):
            if not (row_check(i) and column_check(i) and box_check(i)):
                return False
        return True



