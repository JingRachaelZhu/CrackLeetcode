class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l1 =len(set(nums))      #use set 
        return l1 !=len(nums)