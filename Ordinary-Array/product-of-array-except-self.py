class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # we use left and right list to solve the problem
        # initialize the length
        length = len(nums)
        # initialize the list and answer
        left, right, answer = [0] * length, [0] * length, [0] * length
        
        # do the loop to find the answer
        # we need the answer[i] = left * right[i]
        # so left[i] do not have i, have the left index
        # and right[i] do not have i, have the right index
        left[0], right[length-1] = 1, 1
        for i in range(1,length):
            left[i] = nums[i-1] * left[i-1]
            right[length-1-i] = nums[length-1-i+1] * right[length-1-i+1]
        
        # get the answer
        for i in range(length):
            answer[i] = left[i] * right[i]
        
        return answer
