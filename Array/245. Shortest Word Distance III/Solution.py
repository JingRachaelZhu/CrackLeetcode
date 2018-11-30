class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #one pointer
        dis =len(words)
        a =-1
        for i in range(len(words)):
            if word1 ==word2:               #if two words equal 
                if words[i] ==word1:
                    if a!=-1:
                        dis =min(dis,i-a)
                    a =i
            else:                                           #if they not equal
                if words[i] ==word1 or words[i] ==word2:   
                    if a!=-1 and words[i]!=words[a]:
                        dis =min(dis,i-a)
                    a=i
        return dis

        #more integrated

        # same=(word1 ==word2)

        # for i in range(len(words)):
          
        #     if words[i] ==word1 or words[i] ==word2:
        #         if (a!=-1 and (words[i]!=words[a] or same)):  #make two situations together 
        #             dis =min(dis,i-a)
        #         a=i