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
		if not n: return -1			#edge case
		candidate =0
		for i in range(n):
			if knows(candidate,i):         #find the candidate if others knows him(meanwhile the other can't be the candidate)
				candidate =i
		for i in range(n):
			if i !=candidate and ((i <candidate and knows(candidate,i)) or !knows(i,candidate)):	#check the candidate,i<candidate is a optimal statement which decreases the num of calling knows funtion
				return -1


