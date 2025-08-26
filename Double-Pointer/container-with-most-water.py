class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # first we need to have the length for loop
        n = len(height)
        
        # two pointers from left and right
        left, right = 0, n - 1

        # we need a max_volumn
        max_volumn = 0

        # do the loop to find the max
        while left < right:
            # we need to get the height of the container
            # the height is the minimum number of the left and right
            height_volumn = min(height[left], height[right])
            # get the volumn and compare
            max_volumn = max(max_volumn, height_volumn * (right - left))

            # after that, we need to change left or right
            if height_volumn == height[left]:
                # change the left to get a bigger height
                left += 1
            else:
                right -= 1
        
        return max_volumn
