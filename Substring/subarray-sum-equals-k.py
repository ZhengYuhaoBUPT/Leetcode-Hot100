class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        n = len(nums)
        preSums = defaultdict(int)
        preSums[0] = 1

        presum = 0
        for i in range(n):
            presum += nums[i]

            count += preSums[presum - k]

            preSums[presum] += 1

        return count
