class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        if n * m == 0:
            return n + m

        # DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 边界状态
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(m + 1):
            dp[i][0] = i

        # 计算dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                empty = dp[i-1][j] + 1 # 删除添加
                revise = dp[i-1][j-1] + 1 # 原地修改
                delete = 1 + dp[i][j-1] # 添加删除
                if word1[j-1] == word2[i-1]:
                    revise -= 1

                dp[i][j] = min(empty, revise, delete)

        return dp[m][n]
