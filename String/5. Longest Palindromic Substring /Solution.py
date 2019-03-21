class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #DP
        if not s or len(s) <1: return ""

        start,end =0,0
        len1,len2,maxcur =0,0,0
        for i in range(len(s)):
        	len1 =self.expandFromCenter(s,i,i)    #try odd length 
        	len2 =self.expandFromCenter(s,i,i+1)  #try even length
        	maxcur =max(len1,len2)
        	if maxcur >(end-start):					
        		start =i-(maxcur-1)//2
        		end =i +maxcur//2

        return s[start:end+1]

    def expandFromCenter(self,s,left,right):		
    	while left >=0 and right <len(s) and s[left]==s[right]:
    		left -=1
    		right +=1

    	return right-left-1	      #the length of palindrome