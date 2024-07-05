class Solution:
    def transform(self,s,move):
        c=''
        for i in s:
            asccii=int((ord(i)-96)+move)%26
            if asccii==0:
                char_after_transform='z'
            else:
                char_after_transform=chr(asccii+96)
            c+=char_after_transform
        return c
    def shiftingLetters(self, s: str, shifts) -> str:
        b=''
        for i in range(len(s)):
            b+=s[i]
        for i in range(len(shifts)):
            k=self.transform(b[0:i+1],shifts[i])
            b=''
            b=k
            b+=s[i+1:]
        return b

if __name__=="__main__":
    s = "z"
    shifts = [52]
    a=Solution()
    print(a.shiftingLetters(s,shifts))