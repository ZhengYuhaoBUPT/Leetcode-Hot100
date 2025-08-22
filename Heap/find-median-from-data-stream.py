class MedianFinder(object):

    def __init__(self):
        # we need two heaps to do this
        # First, we need one big heap on the left
        self.left = []
        # Second, we need one small heap on the right
        self.right = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        # before, we define the left heap is geq (greater or equal)
        # if the two heaps is equal, then we first go in to the right
        # to push out the smaller one
        if len(self.left) == len(self.right):
            # heappushpop(self.right, num) first push num then pop smallest
            # because on the left, we finally need to get the bigger one
            # so we need the minus form of all numbers            
            # heappush(self.left, -x) push minus x
            heappush(self.left, -heappushpop(self.right, num))
        else:
            # left length is greater, so we need to do the left first
            heappush(self.right, -heappushpop(self.left, -num))

    def findMedian(self):
        """
        :rtype: float
        """
        
        # if the left is greater, we can just pop the left
        if len(self.left) > len(self.right):
            return -self.left[0] # the smallest one is in 0
        return (self.right[0] - self.left[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
