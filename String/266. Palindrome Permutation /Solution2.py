class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #hashtable
        if not s :return False
        
        dic1 ={}
        for i in s:                          #put every charecter into hashtable
            # if i not in dic1.keys():
            #     dic1[i] =1
            # else:
            #     dic1[i] +=1
            dic1[i] =dic1.get(i,0) +1

        oddcount =0
        #evencount =0
        for value in dic1.values():
            if value %2 !=0:
                oddcount +=1
            # else:
            #     evencount +=1
            if oddcount >1:           
                return false
        return True

        # if evencount ==0:                   #judge Palindrome
        #     if len(set(s)) ==1:
        #         return True
        #     else:
        #         return False
        # else:
        #     if oddcount <=1:
        #         return True
        #     else:
        #         return False
                