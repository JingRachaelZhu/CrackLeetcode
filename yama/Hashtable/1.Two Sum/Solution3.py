class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #sort + two pointer O(nlogn) O(1) 
        
        # left, right 
        
        if not nums: return
        if len(nums) <2: return  #edge case
        
        nums =enumerate(nums)    #
        nums =sorted(nums,key =lambda x:x[1])    #
        
        left, right =0,len(nums)-1
        
        while left <right:
            while nums[left][1]==nums[left+1][1]:left +=1    #if have duplicates nums
            while nums[right][1]==nums[right-1][1]:right-=1  #if have duplicates nums
            
            if nums[left][1]+nums[right][1] <target:
                left +=1
            elif nums[left][1]+nums[right][1] >target:
                right -=1
            else:
                return [nums[left][0],nums[right][0]]
        
        return

# l1 =[7,2,2,3,5]
# tar =9
# A =Solution().twoSum(l1,tar)
# print(A)
        