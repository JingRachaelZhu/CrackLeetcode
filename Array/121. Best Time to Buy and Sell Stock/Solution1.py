class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Kadane's algorithm
        if len(prices) <=1: 
            return 0                        #edge case

        profit =0
        maxcur =0
        for i in range(1,len(prices)):
            maxcur =max(0,maxcur+prices[i]-prices[i-1])     #look for all positive diff 
            profit =max(profit,maxcur)                      
            
        return profit