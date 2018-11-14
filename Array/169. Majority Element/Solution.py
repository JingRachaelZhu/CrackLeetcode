class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #sorting
        res =sorted(nums)		#sorted(iterable) return a new sorted list from the items in iterable.
        #nums.sort()			#.sort() no return 
        return res[len(nums)//2]

        #hashtable(dict)
<<<<<<< HEAD
  #       dic1 =[]
  #       res =0
		# for i in nums:
		# 	# if i not in dic1:
		# 	# 	dic1[i] =1
		# 	# else:
		# 	# 	dic1[i] +=1
		# 	dic1[i] +=dic1.get(i,0)
		# 	if dic1.get(i,0)>len(nums)//2:
		# 		res =i
		# return res
=======
        dic1 =[]
        res =0
	for i in nums:
		# if i not in dic1:
		# 	dic1[i] =1
		# else:
		# 	dic1[i] +=1
		dic1[i] +=dic1.get(i,0)
		if dic1.get(i,0)>len(nums)//2:
			res =i
	return res
>>>>>>> 096e33cee4a942c0907a93ec08435b359e026ad0
