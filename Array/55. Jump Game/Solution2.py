class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #move backfoard from the end
        last =len(nums)-1                   #tag the last position as 'last'
        for i in range(len(nums)-2,-1,-1):
            if i +nums[i]>=last:            #if so,the i position can reach 'last' postion
                last =i
                
        return last==0      