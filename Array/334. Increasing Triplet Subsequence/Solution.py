class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) <=2:return False   #edge case
        small =float('inf')
        middle =float('inf')
        for i in nums:
            if i <=small:
                small =i
            elif i <=middle:
                middle =i
            else:
                return True
        return False