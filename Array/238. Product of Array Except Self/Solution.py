class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left =1
        res =[]
        
        for i in range(len(nums)):      #multiply the nums on the leftside
            res.append(left)
            left *= nums[i]
            
        right =1   
        for j in range(len(nums)-1,-1,-1):      #multiply the nums on the rightside
            res[j] *= right
            right *= nums[j]
            
        return res
        