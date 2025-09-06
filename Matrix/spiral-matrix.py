class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # initialize the row and column
        rows, cols = len(matrix), len(matrix[0])
        # initialize the answer list
        answers = []
        # we need to get the total number
        total = rows * cols
        # initialize the directions
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # initialize the visited number
        visited = [[False] * cols for _ in range(rows)]

        # initialize
        row, col = 0, 0
        directionIndex = 0
        # do the loop
        for i in range(total):
            # choose the direction
            answers.append(matrix[row][col])
            visited[row][col] = True
            # judge the next if can use
            nextrow, nextcol = row + directions[directionIndex][0], col + directions[directionIndex][1]
            if not (0 <= nextrow < rows and 0 <= nextcol < cols and not visited[nextrow][nextcol]):
                # we can not use this
                directionIndex = (directionIndex + 1) % 4
            # get the correct row and col
            row += directions[directionIndex][0]
            col += directions[directionIndex][1]
            
        return answers