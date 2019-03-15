class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return None
        if len(nums) ==1:return 0
       
        left =0
        right =len(nums)-1
        while left < right:
            mid = left +(right -left)/2
            
            
            if nums[mid] < nums[mid+1]:
                left = mid +1           #mid+1 could be the peek item
            else:
                right =mid              #mid could be the peek item
        print(left,right)        
        return left             #finally, left =right point to the peek item