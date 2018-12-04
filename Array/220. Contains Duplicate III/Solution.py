class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        #bucket sort 
        if t<0 or k<=0:return False
        dic1 ={}
        wide =t+1                       # +1 to prevent k ==0,
        for i in range(len(nums)):
            n =nums[i]//wide            # bucket mapping
            if n in dic1:return True
            if n-1 in dic1 and (nums[i]-dic1[n-1]<=t):return True   #either two items in the same bucket or in the adjacent bucket 
            if n+1 in dic1 and (dic1[n+1]-nums[i]<=t):return True
            dic1[n]=nums[i]
            
            if i>=k:del dic1[nums[i-k]//wide]           #Keep as many as k buckets to ensure that the difference is at most k 
        return False
        
        
