class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls =0
        cows =0
        slist =[0 for i in range(10)]
        glist =[0 for i in range(10)]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls +=1
            else:
                slist[int(secret[i])] +=1
                glist[int(guess[i])] +=1
        
        for i in range(10):
            cows +=min(int(slist[i]),int(glist[i]))
            
        #res =str(bulls)+"A"+str(cows)+"B"
        
        return '%dA%dB' % (bulls, cows)