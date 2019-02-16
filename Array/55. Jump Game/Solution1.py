class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Greedy move forward
        
        furthest =0
        for i ,m in enumerate(nums):
            if furthest <i:return False
            furthest =max(i+m,furthest)
            
        return True
            