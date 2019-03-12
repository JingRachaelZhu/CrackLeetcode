class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []    #edge case
        
        res=[]
        
        i =0
        while i < len(nums):
            start =nums[i]      #mark the startpoint of a range
            
            while i+1<len(nums) and nums[i+1]-nums[i] ==1:
                i +=1
            
            if start !=nums[i]:                             #two conditions
                res.append(str(start)+"->"+str(nums[i]))
            else:
                res.append(str(start))                      #only has one num in this range
            i +=1
                
        return res