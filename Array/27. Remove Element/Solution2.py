class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left =0
        right =len(nums)-1
        while left <= right:  						# terminal condition 
            if nums[left]==val:
                nums[right],nums[left] =nums[left],nums[right]  #swap two item
                right -=1
            else:
                left +=1										
        return left
