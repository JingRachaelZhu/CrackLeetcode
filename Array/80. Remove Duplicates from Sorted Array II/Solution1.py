class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0			#edge case
        ct =1
        mark =0
        for i in range(1,len(nums)):
        	if nums[i] !=nums[i-1]:
        		nums[ct] =nums[i]
        		ct +=1
        		mark =0
        	else:
        		mark +=1
        		if mark <2:				#when num of dup is less than 2, reassign it to num[ct]
        			nums[ct] =nums[i]
        			ct +=1

        return ct
