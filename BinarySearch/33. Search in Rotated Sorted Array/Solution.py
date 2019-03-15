class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return -1
        
        left =0
        right =len(nums)-1
         
        while left <= right:
            mid =left +(right -left)/2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:            #[left-mid] is a ascending part
                if nums[left] <=target <=nums[mid]: #check if target in this part
                    right =mid-1
                else:
                    left =mid +1
            else:                                 # [mid-right] is a ascending part
                if nums[mid] <= target <=nums[right]:
                    left = mid +1
                else:
                    right =mid -1
        
        return -1