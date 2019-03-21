class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #binary representation T:O(logn)
        if not x:return None
        
        res =1
        if n <0:
            x =1/x
            n =-n
        i =0
        current =x
        while n >0:
            if n %2 == 1:
                res =res *current
                
            current *=current        # each value for next digit,start from x^0,x^2,x^4...
            n =n/2                  #run at most n/2 steps
            
        
        return res
        