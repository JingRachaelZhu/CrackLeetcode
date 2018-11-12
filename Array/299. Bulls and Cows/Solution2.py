class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #One pass
        bulls =0
        cows =0
        count =[0 for i in range(10)]
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls +=1
            else:
                if count[int(secret[i])] <0:cows +=1     #notice: invert str into int
                if count[int(guess[i])] >0:cows +=1 
                count[int(secret[i])] +=1
                count[int(guess[i])] -=1
        
        return '%dA%dB' % (bulls, cows)