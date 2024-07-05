class Solution:
    def reverse(self,s):
        a=''
        b=s[0:int(len(s)/2)]
        c=s[int(len(s)/2):]
        a=b[::-1]+c
        return a

    def reverseStr(self, s: str, k: int) -> str:
        a=int(len(s)/2/k)
        final=''
        i=0
        while i<a:
            final+=self.reverse(s[i*2*k:i*2*k+2*k])
            i+=1
        b=s[i*2*k:]
        if len(b)<k:
            final+=b[::-1]
        else:
            final+=b[0:k][::-1]+b[k:]
        return final

if __name__=="__main__":
    a=Solution()
    s='abcdghthsdg'
    b=a.reverseStr(s,2)
    print(b)