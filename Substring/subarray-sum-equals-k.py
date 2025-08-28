class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # first we need to initialize the ans
        ans = 0
        n = len(nums)
        # then we need a defaultdict to record the prefix
        cnt = defaultdict(int)
        # we need to record the prefixnumber
        prefix = 0
        # first we need to record the 0 condition
        cnt[0] = 1

        # do the loop, find the number of cnt[k-now_number] add
        for i in range(n):
            # prefix add
            prefix += nums[i]
            # add the number of prefix, we have the equation that
            # prefix - (some number in cnt) = k
            ans += cnt[prefix - k]
            # we need to record how many numbers in (some number in cnt)
            cnt[prefix] += 1

        return ans
