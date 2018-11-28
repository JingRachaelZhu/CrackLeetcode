class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Binary search
        low =1                          #from 1 to n
        high =len(nums)-1
        while high >low:
            mid =low +(high -low)//2    #prevent overflow
            count =0
            for i in nums:
                if i <=mid:
                    count +=1
            if count >mid:              #based on Pigeonhole Principle鸽巢原理
                high =mid               #include mid not mid-1,bcz i<=mid(count+1 when i = mid)
            else:
                low =mid+1
        return low