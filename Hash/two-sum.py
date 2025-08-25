class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # make a hashtable
        hashtable = dict()

        # do the loop, for every number in nums,
        # find if the target - number in hashtable
        # if exist, return [hashtable[target-number], nums[i]]
        # else, add num
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [hashtable[target-nums[i]], i]
            hashtable[nums[i]] = i
