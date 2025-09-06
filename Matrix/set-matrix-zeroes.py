class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # initialize the row and colomn
        row, col = len(matrix), len(matrix[0])
        # initialize bool judgement
        row_judge, col_judge = [False] * row, [False] * col

        # do the loop to find the 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_judge[i] = col_judge[j] = True
            
        # revise the matrix
        for i in range(row):
            for j in range(col):
                if row_judge[i] or col_judge[j]:
                    matrix[i][j] = 0