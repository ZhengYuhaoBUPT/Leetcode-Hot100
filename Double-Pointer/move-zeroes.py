class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # first get the length of the nums
        n = len(nums)

        # use two pointers
        # the left and right both start at index 0
        # if num is not 0, both the pinter go and left = num
        # else num is 0, the right pointer go, left do not go, zeronums+1
        left = right = 0

        # the number of zero
        zero_number = 0

        # two loop, first find 0, second revise last few nums to zero
        # do the first loop
        while right < n:
            if nums[right] == 0:
                zero_number += 1
            else:
                nums[left] = nums[right]
                left += 1
            right += 1

        # do the second loop
        while zero_number > 0:
            nums[n - zero_number] = 0
            zero_number -= 1
    
