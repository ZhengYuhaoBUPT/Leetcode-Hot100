class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # initialize the length
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                # the symetry around center is easy, just n-1-x
                # if rotated 90 degrees, we have 
                matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] \
                = matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]