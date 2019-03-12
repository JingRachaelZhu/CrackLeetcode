class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emailset =set()             #use set structure
        
        # for i in emails:
        #     tmp2 =i.find("@")
        #     newlocal =i[:tmp2].replace(".","")
        #     tmp1 =newlocal.find("+")
        #     newemail =newlocal[:tmp1]+i[tmp2+1:]
        #     emailset.add(newemail)
        
        for email in emails:
            email =email.split("@")         #split into local and domain parts
            local =email[0]
            demain =email[1]
            local =local.split("+")[0].replace(".", "")
            newemail =local+"@"+demain
            emailset.add(newemail)
            
        return len(emailset)
            
        
        