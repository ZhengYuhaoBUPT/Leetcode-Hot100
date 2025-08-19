class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        p0, p1 = 0, 0
        n = len(nums)
        # find the smaller number from the back
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # if the nums is always going down
        if i >= 0:
            # find the bigger number from the front
            j = n - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            # exchange the two numbers
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, n - 1
        # do the sort
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
