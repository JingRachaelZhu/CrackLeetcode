class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        
        res =1
        for i in range(len(nums)):
            if res in nums:
                res +=1
            else:
                return res
        return res
        
        #T(n) = O(n^2), S(n) = O(1)