class Solution:
    def largeGroupPositions(self, s: str) :
        group=[]
        a=''
        i=0
        while i<len(s):
            if a=='':
                a+=s[i]

            else:
                if s[i]==a[-1]:
                    a+=s[i]

                else:
                    i-=1
                    group.append(a)
                    a=''
            i+=1
        group.append(a)

        index=0
        ls_final=[]
        for i in range(len(group)):
            l=len(group[i])
            if l>=3:
                ls_final.append([index,index+l-1])
                index+=l
            else:
                index+=l
        return ls_final


if __name__=="__main__":
    a=Solution()
    s="aaa"
    print(s)
    b=a.largeGroupPositions(s)
    print(b)
