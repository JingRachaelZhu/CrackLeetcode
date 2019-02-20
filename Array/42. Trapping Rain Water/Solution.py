class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #two pointer update version of No.11
        left =0
        right =len(height)-1
        maxleft =0
        maxright =0
        res =0
        while left <right:                     
            if height[left] <height[right]:         #set 2 barriers and 1 line in the middle
                maxleft =max(maxleft,height[left])
                res +=maxleft-height[left]          #the diff is the are of water
                left +=1
            else:
                maxright =max(maxright,height[right])
                res +=maxright-height[right]
                right -=1
        
        return res