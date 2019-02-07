class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #sliding windows
        s1 =set()
        if k<0:return False
        if k>len(nums):k =len(nums)-1
        
        for i in range(len(nums)):
            if i>k:
                s1.remove(nums[i-k-1])     #keep the len of set to k
            if nums[i] in s1:return True   #if nums[i] exists, then the dis must be at mosts k.
            s1.add(nums[i])
            
        return False
        