class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #use zip
        res =[1]
        for i in range(rowIndex):
        	res =[x+y for x,y in zip([0]+res,res+[0])]     #use zip to produce two lists for addition 
        return res

        #use map,(Return an iterator on Python3 while a list on Python2) 
	res =[[1]]
	for i in range(rowIndex):
		A =list(map(lambda x,y:x+y ,[0]+res[-1],res[-1]+[0]))  #convert map to list
		res +=[A]
	return res[rowIndex]
