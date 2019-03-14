class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        #two pointers
        if not nums or sum(nums) < s:return 0   #edge case
        
        i =0
        start =0
        sumcur =0
        minlen =len(nums)+1
        while i <len(nums):
            sumcur += nums[i]
            
            while sumcur >=s:                   #adjust sumcur and start point
                minlen =min(minlen,i-start+1)
                sumcur -=nums[start]
                start +=1
            i +=1
        
        return minlen
                
        
        