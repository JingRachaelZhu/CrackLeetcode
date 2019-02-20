class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #set
        if not nums:                #edge case
            return 0
        if len(nums) ==1:
            return 1
        
        length =0
        nums =set(nums)             #set array 
        while nums:
            value =nums.pop()       #once visited,remove it  
            left =0
            right =0
            former =value-1
            later =value+1
            while former in nums:       #O(1),cuz set(array) 
                nums.remove(former)     #once visited,remove it
                former -=1
                left +=1
            while later in nums:        #O(1)
                nums.remove(later)
                later +=1
                right +=1
            length =max(length,left+1+right)
            
        return length
        