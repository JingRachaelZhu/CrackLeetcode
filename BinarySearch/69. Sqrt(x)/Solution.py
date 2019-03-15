class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #binary_search
        if x ==0:return 0       #edge case
        
        left =1
        right =x                #the range[1,x]
        while left <=right:
            mid =left +(right -left)/2
            
            if mid > x/mid:     #key condition
                right =mid -1
            elif mid +1 > x/(mid +1):   #the decimal digits are eliminated
                return mid
            else:
                left =mid +1
                
        
                
            
        