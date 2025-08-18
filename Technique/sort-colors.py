class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # using two pointers
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
# 双指针
# 因为有三种数字
# 左边的指针时钟在等着新的0出现，因为有可能会有新的0
# 右边的指针不断向前更新
