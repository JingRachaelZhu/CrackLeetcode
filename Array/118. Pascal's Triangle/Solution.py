class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:return []
        res =[[1]*(i+1) for i in range(numRows)]	#res:[[1],[1,1],[1,1,1],...]
        for i in range(numRows):
              for j in range(1,i):
                    res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res