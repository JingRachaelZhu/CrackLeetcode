class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #hash table O(n) O(n)
        
        # key value 
        # 2     0    look for 7
        # 7     1    look for 2
        # 11    2
        # 15    3
        
        # for item in list:
        #     if target-item in dict:
        #         return [index,dic[ele]] 
            
        #     put item in dict
        if not nums: return
        if len(nums) <2: return  #edge case
        
        dic1 =dict()
        for i in range(len(nums)):
            if target-nums[i] in dic1:
                return [dic1[target-nums[i]],i]
            
            dic1[nums[i]] =i
            
        
        return 