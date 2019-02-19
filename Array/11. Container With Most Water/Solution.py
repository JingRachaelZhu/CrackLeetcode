class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #two pointers 
        area =0
        left =0
        right =len(height)-1
        while left <right:
            area =max(area,(right-left)*min(height[left],height[right]))
            if height[left] <height[right]:            #the smaller line is the key factor of the area of the container.
                left +=1
            else:
                right -=1
        
        return area