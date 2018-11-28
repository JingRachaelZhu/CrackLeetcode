class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Two pointer (fast&slow)
        slow =nums[0]                   #if dups exists,cycle does exists
        fast =nums[nums[0]]
        while fast !=slow:              #when they meet,the distance is exactly the n length of the cycle
            slow =nums[slow]
            fast =nums[nums[fast]]
        
        fast =0
        while fast !=slow:              #find the entry point--dup num
            slow =nums[slow]
            fast =nums[fast]
            
        return slow