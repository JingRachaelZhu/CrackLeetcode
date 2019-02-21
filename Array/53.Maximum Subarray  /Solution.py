class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #k algo
        if not nums :return 
        
        
        maxsum =nums[0]
        maxcur =nums[0]
        for i in nums[1:]:
            maxcur =max(i,maxcur+i)
            maxsum =max(maxsum,maxcur)
            
        return maxsum
        