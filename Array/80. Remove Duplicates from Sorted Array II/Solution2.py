class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct =0
        for num in nums:
        	if i<2 or num >nums[ct-2]:		#it at most appears twice in the updated array 
        		nums[ct] =num
        		ct +=1
        return ct