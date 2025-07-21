class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = len(nums)
        left, right = 0, n - 1
        ans = n
        
        while left <= right:
            mid = left + (right - left) / 2
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
