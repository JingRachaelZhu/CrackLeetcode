class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0			#edge case
        ct =1
        for i in range(1,len(nums)):	#from second item to the end
        	if nums[i] !=nums[i-1]:		#compare in pairs
        		nums[ct] =nums[i]
        		ct +=1
        return ct
