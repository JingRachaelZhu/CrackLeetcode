class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #oyer-Moore Majority Vote algorithm 摩尔投票算法
        if not nums:return []
        can1,can2 =0,1
        count1,count2 =0,0
        for n in nums:                          #select candidates
            if n ==can1:
                count1 +=1
            elif n ==can2:
                count2 +=1
            elif count1 ==0:
                can1 =n
                count1 =1
            elif count2 ==0:
                can2 =n
                count2 =1
            else:
                count1 -=1
                count2 -=1
        res =list()
        for i in (can1,can2):                   #verify the correctness of candidates
            if nums.count(i) >len(nums)//3:
                res.append(i)
        
        # if nums.count(can2) >len(nums)//3:
        #     res.append(can2)
        return res
        