class Solution:
    def check(self,s):
        ls=list(s)
        ls1=list(set(ls))
        if len(ls1)==1:
            return False
        return True
    def longestNiceSubstring(self, s: str) -> str:
        i=0
        sub_nice_string=[]
        while i<len(s):
            a=''
            a+=s[i]
            if i==len(s)-1:
                sub_nice_string.append(a)
                break
            else:
                j=i+1
                while s[i].upper()==s[j].upper():
                    a+=s[j]
                    j+=1
                    if j>len(s)-1:
                        break
                sub_nice_string.append(a)
                i=j

        sub_nice_string1=[]
        for i in range(len(sub_nice_string)):
            if self.check(sub_nice_string[i]):
                sub_nice_string1.append(sub_nice_string[i])
            else:
                sub_nice_string1.append(' ')

        # return sub_nice_string1
        i=0
        ls_final=[]
        while i<len(sub_nice_string1):
            if i==len(sub_nice_string1)-1:
                if sub_nice_string1[i]!=' ':
                    ls_final.append(sub_nice_string1[i])
                    break
                else:
                    break
            else:
                a=''
                j=i+1
                if sub_nice_string1[i]==' ':
                    i+=1
                else:

                    a+=sub_nice_string1[i]

                    while sub_nice_string1[j]!=' ':
                        a+=sub_nice_string1[j]
                        j+=1
                        if j>len(sub_nice_string1)-1:
                            break
                    ls_final.append(a)
                    i=j

        if ls_final==[]:
            return ''
        max_sub_nice = len(ls_final[0])
        sub_nice_max = ls_final[0]
        for i in range(len(ls_final)):
            if len(ls_final[i]) > max_sub_nice:
                max_sub_nice = len(ls_final[i])
                sub_nice_max = ls_final[i]
        return sub_nice_max



if __name__=="__main__":
    s="YazaAay"
    a=Solution()
    b=a.longestNiceSubstring(s)
    print(b)

    '''chua gia quyet duoc'''