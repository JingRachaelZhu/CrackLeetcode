# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
 
class Solution(object):
	def findCelebrity(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		#T(n) =O(n^2),S(n) =O(n)
		if not n:return 0
		res =list(True for i in range(n))    
	 
		for i in range(n):
			for j in range(n):
				if i ==j:
					continue
				elif not knows(i,j):		#if i doesnt kn j,j not celebrity
					res[j] =False
				else:						#if i kn j,i not celebrity
					res[i] =False
					
		for i in range(n):
			if res[i] ==True:
				return i
		return -1

		#improve solution,optimize the space complexity(no need new array)

		# cele =-1
		# for i in range(n):
		# 	mark =True
		# 	for j in range(n):
		# 		if i !=j and knows(i,j):
		# 			mark =False
		# 			break
		# 	if mark:                     #find the candidate depending on key1:cele kns noone
		# 		cele =i
		# 		break


		# if cele != -1:
		# 	for i in range(n):
		# 		if i !=cele and not knows(i,cele):		#check the key2:everyone kns cele
		# 			return -1
		# return cele

