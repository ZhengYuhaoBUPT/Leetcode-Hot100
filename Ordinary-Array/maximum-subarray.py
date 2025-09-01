class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # get the length
        length = len(nums)
        # initialize a list for recording the length at this time
        len_list = [0] * length
        # first add the 0 index
        len_list[0] = nums[0]

        # do the loop to find the max length
        for i in range(1,length):
            # if the sum before is smaller than 0, then skip
            # else, we need the number before
            len_list[i] = max(len_list[i-1],0) + nums[i]

        return max(len_list)
