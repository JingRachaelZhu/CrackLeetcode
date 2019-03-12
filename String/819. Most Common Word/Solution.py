class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        # str1 = paragraph.replace(","," ")
        # str1 = str1.replace("."," ")
        # str1 = str1.replace("!"," ")
        # str1 = str1.replace("?"," ")
        # str1 = str1.replace(";"," ")
        # str1 = str1.replace("'"," ")
        # str1 = str1.split()
        str1 =paragraph.lower()
        str1 =re.findall(r"\w+", str1)      # 正则表达式
        maxcnt =0
        count =dict()                   #use hashtable to recored the counts
        res =[]
        nanned =set(banned)             #use set structure to store banned
        for i in str1:      
            if i in banned:             #`in` set is O(1)
                continue
                
            # if i in count:
            #     count[i] +=1
            # else:
            #     count[i] =1
            count[i] =count.get(i,0)+1
           
            if count[i] >maxcnt:
                maxcnt =count[i]
                #res =i
                        
        for i,j in count.items():       #have at least two most frequent words
            if j ==maxcnt:
                res.append(i)
            
        return ''.join(res)             #convert list to string
            
        