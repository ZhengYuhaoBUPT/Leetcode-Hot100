class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_steak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_steak += 1

                longest = max(longest, current_steak)

        return longest
