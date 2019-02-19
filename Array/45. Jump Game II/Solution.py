class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #BFS with greedy
        
        jump =0
        end =0
        furthest =0
        for i in range(len(nums)-1):         #i meand current point
            furthest = max(furthest,i+nums[i])
            if i==end:                       #if it reaches the boundary of step range ,jump to next level
                jump +=1                      #jump to next level
                end =furthest               #define the next level size
                
        return jump