class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left, right = 0, len(height) - 1
        max_volume = 0

        while left < right:
            high = min(height[left], height[right])
            max_volume = max(max_volume, high * (right - left))
            if high == height[left]:
                left += 1
            else:
                right -= 1

        return max_volume
