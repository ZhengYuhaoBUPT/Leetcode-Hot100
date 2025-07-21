class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        maxlength = 0
        n = len(nums)
        if n <= 1:
            return True

        for i in range(n):
            if maxlength >= i:
                maxlength = max(maxlength, i + nums[i])
                
                if maxlength >= n - 1:
                    return True
        return False
