class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k =k%len(nums)

        # def reverse(num,start,end):
        # 	while(start<end):
        # 		tmp =num[start]
        # 		num[start] =num[end]
        # 		num[end] =tmp
        # 		start +=1
        # 		end -=1

        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
        def reverse(num,start,end):
        	while(start<end):
        		tmp =num[start]
        		num[start] =num[end]
        		num[end] =tmp
        		start +=1
        		end -=1