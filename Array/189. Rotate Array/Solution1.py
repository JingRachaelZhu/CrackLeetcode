class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:return 
        if k>len(nums):         #if k is large num, the useful thing is the remainder.
            k =k%len(nums)
    
        for i in range(k):
            tmp =nums.pop()     #pop from the end
            nums.insert(0,tmp)  #add from the head
        