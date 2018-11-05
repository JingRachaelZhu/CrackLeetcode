class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1

        i =0
        while i < len(nums):
            cur =nums[i]
            if cur >0 and cur <=len(nums) and nums[cur-1] !=cur:   #if the corresponding position is occupied with wrong num,replace it with correct num.
                nums[cur-1],nums[i]=nums[i],nums[cur-1]
                
            else:       
                i +=1
                
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1