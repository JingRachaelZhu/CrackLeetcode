class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        
        self.dict ={}
        for i,n in enumerate(words):
            self.dict[n] =self.dict.get(n,[])+[i]
        """ 
        from collections import defaultdict   #do'nt forget to import module
        self.dic =defaultdict(list)          # initialize value to an empty list
        for i,n in enumerate(words):
            self.dic[n].append(i)            #simpler and faster than an equivalent technique using dict.setdefault()
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 =self.dic[word1]
        l2 =self.dic[word2]
        dis =float("inf")
        length1,length2=len(l1),len(l2)
        i,j =0,0
        while i<length1 and j<length2:
            
            if l1[i] <l2[j]:
                dis =min(dis,l2[j]-l1[i])
                i +=1
            else:
                dis =min(dis,l1[i]-l2[j])
                j +=1
        return dis
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)