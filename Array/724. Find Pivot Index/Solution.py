class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return -1
        left =0
        right =sum(nums)
        for i in range(len(nums)):
            right -=nums[i]
            #left +=(nums[i-1] if i!=0 else 0) 
            if right == left:
                return i
            left +=num[i]
        return -1
        