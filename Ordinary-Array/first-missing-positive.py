class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # initialize the length
        length = len(nums)
        # we do not care about negative numbers
        for i in range(length):
            if nums[i] <= 0:
                # we just redefine the number to make sure have
                # no influence
                nums[i] = length + 1
        # do the loop, if the number i is smaller than length
        # then we can set the index nums[i] negative to distinct
        for i in range(length):
            if abs(nums[i]) <= length:
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        # after the loop, we find the smallest i larger than 0
        for i in range(length):
            if nums[i] > 0:
                return i + 1
        
        return length + 1
