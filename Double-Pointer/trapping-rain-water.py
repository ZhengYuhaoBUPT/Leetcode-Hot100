class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # three pointers
        left, right = 0, len(height) - 1
        sum_volumn = 0
        left_volumn, right_volumn = height[left], height[right]
        
        while left < right:
            left_volumn = max(left_volumn, height[left])
            right_volumn = max(right_volumn, height[right])

            # move mid
            if height[right] > height[left]:
                sum_volumn += left_volumn - height[left]
                left += 1
            else:
                sum_volumn += right_volumn - height[right]
                right -= 1
                
        return sum_volumn
