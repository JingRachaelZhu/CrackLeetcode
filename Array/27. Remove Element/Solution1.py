class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ct =0
        for i in range(len(nums)):
            if nums[i] !=val:
                nums[ct] =nums[i]     #reassign the value of the list from beginning
                ct +=1
        return ct