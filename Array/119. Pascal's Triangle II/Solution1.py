class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res =[0]*(rowIndex+1)        #res :[0,0,...,0]
        res[0]=1
        for i in range(1,rowIndex+1):
        	for j in range(rowIndex,0,-1):
        		res[j] +=res[j-1]
        return res

