class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        dpmax = [0] * (n)
        dpmin = [0] * (n)
        dpmax[0] = dpmin[0] = nums[0]

        for i in range(1, n):
            x = nums[i]
            dpmax[i] = max(dpmax[i - 1] * x, x, dpmin[i - 1] * x)
            dpmin[i] = min(dpmax[i - 1] * x, x, dpmin[i - 1] * x)

        return max(dpmax)
