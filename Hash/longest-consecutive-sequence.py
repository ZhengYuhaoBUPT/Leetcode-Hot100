class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # record the longest number
        longest = 0

        # transform the nums into set
        nums_set = set(nums)

        # do the loop to try all num in nums, find if num - 1 exist
        for num in nums_set:
            # if we try every number may beyond the time
            # then, we just skip some
            # only if num + 1 not in set, we do
            # else the length must be shorter
            if num + 1 not in nums_set:
                # tmp for length of the num at this time
                tmp = 1
                # check nums - 1, use while for consecutive number before
                while num - 1 in nums_set:
                    tmp += 1
                    num -= 1

                # we need to choose the maximum length
                longest = max(longest, tmp)
        
        return longest
