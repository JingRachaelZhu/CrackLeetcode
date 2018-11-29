class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #one pointer
        dis =len(words)
        index =-1
        
        for i in range(len(words)):
            if words[i]==word1 or words[i]==word2:
                if index !=-1 and words[index]!=words[i]:       #make sure find both word1 and word2
                    dis =min(dis,i-index)
                index =i
          
        return dis
                
        