class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #sort
        if not citations :return 0			#edge case
        length =len(citations)
        citations.sort()
        for i in range(len(citations)):
            if citations[i]>=length-i:
                return length-i
            
        return 0