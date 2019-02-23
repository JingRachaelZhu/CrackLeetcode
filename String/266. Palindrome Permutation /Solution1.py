class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #set
        if not s:return False    #edge case
        
        set1 =set()
        for i in s:
            if i not in set1:
                set1.add(i)
            else:
                set1.remove(i)
                
        return len(set1)<=1      #the Palindrome condition
                