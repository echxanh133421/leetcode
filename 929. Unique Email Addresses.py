class Solution:
    def process(self,email):
        local=''
        domain=''
        for i in range(len(email)):
            if email[i]=='@':
                domain=email[i+1:]
                break
        for i in range(len(email)):
            if email[i]=='+' or email[i]=='@' :
                break
            elif email[i]=='.':
                pass
            else:
                local+=email[i]
        return local+'@'+domain



    def numUniqueEmails(self, emails) :
        ls=[]
        for email in emails:
            a=self.process(email)
            if ls==[]:
                ls.append(a)
            else:
                if a not in ls:
                    ls.append(a)
        return len(ls)

if __name__=='__main__':
    a=Solution()
    emails=["test.email+alex@leetcode.com", "test.email@leetcode.com"]
    b=a.numUniqueEmails(emails)
    print(b)