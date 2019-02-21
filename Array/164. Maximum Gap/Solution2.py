class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #sort
        if not nums or len(nums) <=1:return 0
        
        
        res =0
        former =0
        nums =sorted(nums)
        for i in range(1,len(nums)):
            former =nums[i-1]
            res =max(res,nums[i]-former)
            
        return res