class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        dp = [[0] * i for i in range(1, numRows + 1)]

        for i in range(numRows):
            dp[i][0] = 1
            dp[i][i] = 1

        res = []
        for i in range(numRows):
            for j in range(i):
                if i != 0 and j != 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            res.append(dp[i])

        return res
