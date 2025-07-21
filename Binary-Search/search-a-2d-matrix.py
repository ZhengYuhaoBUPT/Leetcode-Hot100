class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while j >= 0 and i < m:
            if matrix[i][j] == target:
                return True
            if target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        
        return False
