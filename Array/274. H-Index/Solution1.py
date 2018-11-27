class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #bucket sort
        if not citations :return 0
        l1 =[0 for i in range(len(citations)+1)]        #create a bucket array
        for n in citations:                             #count the values into buckets
            if n<=len(citations):
                l1[n] +=1
            else:
                l1[-1] +=1

        count =0
        for i in range(len(citations),-1,-1):           #caculate nums on each bucket from end to head
            count +=l1[i]
            if count>=i:
                return i  
            
        return 0
        