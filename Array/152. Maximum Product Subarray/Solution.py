class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcur =nums[0]         #keep tack of maxcur and mincur 
        mincur =nums[0]
        res =nums[0]
        
        for n in nums[1:]:
            if n < 0:              #if num < 0, the maxcur would be the mincur*num or the num itself
                tmp =maxcur
                maxcur =mincur
                mincur =tmp
            
            maxcur =max(maxcur*n,n)
            mincur =min(mincur*n,n)
            
            res =max(res, maxcur)
            
        return res
        
        
        