class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # have the length
        n = len(height)
        # initialize two pointers
        left, right = 0, n - 1
        # get the max_height of the left and right
        max_left, max_right = height[left], height[right]
        # total volumn
        volumn = 0

        # do the loop while left < right
        # for left: if the next height is bigger, change height
        # else if is smaller, add the volumn
        # and we always do the smaller one between right and left.
        while left < right:
            # left is smaller, change left
            if max_left < max_right:
                left += 1
                # add the volumn for the left index 
                volumn += max(0, max_left - height[left])
                # change the height
                max_left = max(max_left, height[left])
            # same to the right
            else:
                right -= 1
                # add the volumn for the left index 
                volumn += max(0, max_right - height[right])
                # change the height
                max_right = max(max_right, height[right])

        return volumn
