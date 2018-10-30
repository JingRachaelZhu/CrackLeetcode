class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:return 
        if k>len(nums):
            k =k%len(nums)
        #slice assigment
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]   #get slice O(n)