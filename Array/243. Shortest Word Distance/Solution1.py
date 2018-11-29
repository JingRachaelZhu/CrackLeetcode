class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #Two pointer
        dis =len(words)                             #dis is not greater than length of the array
        a =-1
        b =-1
        for i in range(len(words)):
            if words[i]==word1:
                a =i
                if b!=-1:dis =min(a-b,dis)          #without using abs
            elif words[i]==word2:
                b =i
                if a!=-1:dis =min(b-a,dis)
            #if a!=-1 and b!=-1:
                #dis =min(abs(a-b),dis)
        return dis
                
        