class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # first we need to sort the nums
        nums.sort()

        # the length
        n = len(nums)

        # the answer
        answer = []

        # then, we need to do the loop from the first
        for first in range(n):
            # we do not need the same first
            if first > 0 and nums[first] == nums[first-1]:
                continue
            # for every first number, find the second and the third
            third = n - 1
            # do the loop for second
            for second in range(first + 1, third):
                # cancel the same number
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                # the answer is bigger than 0
                while second < third and nums[second] + nums[third] > -nums[first]:
                    # get smaller
                    third -= 1
                # second and third can not be the same
                if second == third:
                    break
                if nums[second] + nums[third] == -nums[first]:
                    answer.append([nums[first], nums[second], nums[third]])
        
        return answer
