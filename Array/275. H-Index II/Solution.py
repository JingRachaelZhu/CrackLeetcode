class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #sort
        if not citations :return 0			#edge case
        
        left,right =0,len(citations)-1
        length =len(citations)
        while left <=right:                 #need = if only one element in the array
            mid =(left+right)//2
            if citations[mid] == length-mid:  #means 'length-mid' of all papers have at least 'citations[mid]' citations each
                return length-mid 
            elif citations[mid] > length-mid:
                right =mid-1
            else:
                left =mid+1
            
        return length-(right+1)               #if not hit the target ,the target will be on the between of right and left.