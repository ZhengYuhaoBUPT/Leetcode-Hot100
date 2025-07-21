class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dp = [0] + [n]* (n)
        for num in nums:
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[-1]
