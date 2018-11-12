class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:return []
        res =[[1]*(i+1) for i in range(numRows)]	#initilize all 1 in each list
        for i in range(numRows):
              for j in range(1,i):
                    res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res