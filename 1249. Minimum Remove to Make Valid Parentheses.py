class Solution:
    def minRemoveToMakeValid(self, s) :
        ls_=[]
        ls_index=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]==')':
                if ls_==[]:
                    ls_.append(s[i])
                    ls_index.append(i)
                else:
                    if ls_[-1]=='(' and s[i]==')':
                        ls_=ls_[:-1]
                        ls_index=ls_index[:-1]
                    else:
                        ls_.append(s[i])
                        ls_index.append(i)

        #return ls_
        b=s
        count=0
        for i in ls_index:
            index=i-count
            s1=b[0:index]
            s2=b[index+1:]
            b=s1+s2
            count+=1
        return b
if __name__=="__main__":
    s='))(('
    a=Solution()
    b=a.minRemoveToMakeValid(s)
    print(b)
