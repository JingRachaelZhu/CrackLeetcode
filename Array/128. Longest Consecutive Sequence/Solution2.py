class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dict
        if not nums:                    #edge case
            return 0
        if len(nums) ==1:
            return 1
        
        dic1 =dict()
        longest =0
        for i in nums:
            if i in dic1:continue
                
            dic1[i]=1
            left,right =0,0             #represent the left and right sequeue
            if i-1 in dic1:
                left =dic1[i-1]                 #take the length of left sonsecutive sequeue
            if i+1 in dic1:
                right =dic1[i+1]
            longest =max(longest,left+1+right)
            
            dic1[i-left]=left+1+right           #update the length(value) of boundary item(key)
            dic1[i+right]=left+1+right          #replace the value of boundary with new length
        
        return longest