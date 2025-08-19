class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)

        # # loop for duplicate
        # # have this number
        # for tmp in range(n):
        #     for i in range(n):
        #         if i != tmp and nums[i] == nums[tmp]:
        #             return nums[tmp]


        fast, slow = 0, 0
        # find the encounter point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # put fast in the place, slow in the begin
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
