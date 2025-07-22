class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        sumAll = sum(nums)
        if sumAll % 2:
            return False
        
        target = sumAll // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        
        return dp[-1]
