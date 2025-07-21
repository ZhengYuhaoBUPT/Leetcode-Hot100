class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]

        total = rows * columns
        results = []

        row, column = 0, 0
        
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0
        
        for i in range(total):
            results.append(matrix[row][column])
            visited[row][column] = True

            nextrow, nextcolumn = row + direction[directionIndex][0], column + direction[directionIndex][1]
            if not (0 <= nextrow < rows and 0 <= nextcolumn < columns and not visited[nextrow][nextcolumn]):
                directionIndex = (directionIndex + 1) % 4

            row += direction[directionIndex][0]
            column += direction[directionIndex][1]
            
        return results
