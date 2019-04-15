class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #brute force O(n^2) O(1)
        
        # 2: 7 11 15  look for 7
        # 7: 11 15   look for 2
        # 11: 15   look for -2
        # 15:       look for -6   
        
        if not nums :return None
        if len(nums) <=1 :return None   #edge cases
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):    
                temp  =target -nums[i]
                if nums[j] ==temp:
                    return [i,j]
                
        return None