class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        #binary search
       	result = len(nums) + 1
	    for idx, n in enumerate(nums[1:], 1):
	        nums[idx] = nums[idx - 1] + n        #accumulative sum
	    left = 0
	    for right, n in enumerate(nums):
	        if n >= target:
	            left = self.find_left(left, right, nums, target, n)
	            result = min(result, right - left + 1)
	    return result if result <= len(nums) else 0

	def find_left(self, left, right, nums, target, n):   #binary search
	    while left < right:
	        mid = (left + right) // 2
	        if n - nums[mid] >= target:
	            left = mid + 1
	        else:
	            right = mid
	    return left