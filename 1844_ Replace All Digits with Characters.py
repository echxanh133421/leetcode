class Solution:
    def shift(self,a,b):
        return chr(ord(a)+int(b))

    def replaceDigits(self, s: str) -> str:
        ls=[]
        i=0
        if len(s)==1:
            return s
        # while i<len(s):
        #     if i%2==0:
        #         ls.append(s[i])
        #     else:
        #         char=self.shift(s[i-1],s[i])
        #         ls.append(char)
        #     i+=1
        # return ''.join(ls)
        while i<len(s):
            ls.append(s[i])
            char=self.shift(s[i],s[i+1])
            ls.append(char)
            i+=2
        return ''.join(ls)
if __name__=="__main__":
    s = "a1c1e1"
    a=Solution()
    print(a.replaceDigits(s))
