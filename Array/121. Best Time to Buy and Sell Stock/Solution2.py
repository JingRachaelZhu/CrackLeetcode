class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <=1: 
            return 0                        #edge case

        profit =0
        minnum =float("inf")
        for i in prices:
            minnum =min(minnum,i)           #find the smallest value
            profit =max(profit,i-minnum)    #keep track of most profit
            
        return profit