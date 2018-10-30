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
		#Queue(FIFO) solution
		if not n:return 0					#edge case
		queue =list(i for i in range(n))
		while (len(queue)>1):
			A =queue.pop()              #assume the tail of array as the head of the queue
			B =queue.pop()
			if knows(A,B):
				queue.insert(0,B)		#add the candidate to the tail of queue
			else:
				queue.insert(0,A)
		cele =queue.pop()				#get the final candidate
		for i in range(n):				#check the candidate
			if i !=cele and (knows(cele,i) or not knows(i,cele)):
				return -1
		return cele


		#Stack(FILO) solution
		if not n:return 0
		stack =list(i for i in range(n))
		A =stack.pop()
		B =stack.pop()
		#while (len(stack)>1):
		while stack:
			if knows(A,B):				#compare two persons each time in order
				A=stack.pop()
			else:
				B=stack.pop()
		#cele =stack.pop()      #need to check the last person with A and B,respectively
		# if knows(cele,A):
		# 	cele =A
		# if knows(cele,B):
		# 	cele =B
		if knows(A,B):			
			cele =B
		else:
			cele =A
		for i in range(n):		#check the candidate 
			if i !=cele and (knows(cele,i) or not knows(i,cele)):
				return -1
		return cele

			 