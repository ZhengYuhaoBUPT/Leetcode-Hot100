class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # first we need to get the length
        m, n = len(matrix), len(matrix[0])
        # initialize the first search place then loop
        # we start from the top left index
        # because in this place, we can split greater and less
        # if greater, x plus 1, else y plus 1
        x, y = 0, n - 1
        
        # do the loop
        while x < m and y >= 0:
            # we need to ensure that not exceed
            if matrix[x][y] == target:
                return True
            if target > matrix[x][y]:
                # we need to minus 1 to y
                x += 1
            else:
                y -= 1

        # no target
        return False