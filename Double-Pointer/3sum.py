class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        results = list()
        n = len(nums)

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            
            third = n - 1
            target = - nums[first]

            # two number
            for second in range(first + 1, third):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                
                if second == third:
                    break
                    
                if nums[second] + nums[third] == target:
                    results.append([nums[first], nums[second], nums[third]])

        return results
