class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <=1:return 0    #edge case
        
        diff =0
        profit =0
        for i in range(1,len(prices)):
            diff =max(0,prices[i]-prices[i-1])
            profit +=diff
            
        return profit