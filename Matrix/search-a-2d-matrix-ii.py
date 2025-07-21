class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1

        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        
        return False
