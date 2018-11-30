class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #hashtable
        dic1={}
        for i,n in enumerate(nums):
            if n in dic1 and i-dic1[n] <=k:   #convert pb to logical one
                return True
            
            dic1[n]=i
                  
        return False
                    