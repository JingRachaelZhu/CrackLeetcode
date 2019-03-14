class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #hashtable + two pointers
        if s is None :return 0
        if len(s) ==1 :return 1
        
        char =dict()
        start =0
        i =0
        maxlen =0
        while i < len(s):
            if s[i] not in char:
                char[s[i]] = i
            else:
                maxlen =max(maxlen,i-start)
                if start < char[s[i]]+1:      #start can only move forward
                    start  =char[s[i]]+1
                char[s[i]] =i
                
            i +=1
        maxlen =max(maxlen,i-start)
            
        return maxlen
                