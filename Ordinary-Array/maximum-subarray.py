class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # ans = -inf
        # min_pre_sum = presum = 0
        # for x in nums:
        #     presum += x
        #     ans = max(ans, presum - min_pre_sum)
        #     min_pre_sum = min(min_pre_sum, presum)

        # return ans

        f = [0] * len(nums)
        f[0] = nums[0]

        for i in range(1, len(nums)):
            f[i] = max(f[i-1], 0) + nums[i]

        return max(f)
