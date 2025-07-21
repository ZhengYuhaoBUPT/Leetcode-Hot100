class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        minprice = 1e9
        maxprofit = 0

        for price in prices:
            maxprofit = max(maxprofit, price - minprice)
            minprice = min(price, minprice)

        return maxprofit
