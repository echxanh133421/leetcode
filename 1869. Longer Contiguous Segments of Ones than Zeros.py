class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        len_1=0
        len_0=0
        i=0
        while i<len(s):
            if s[i]=='1':
                max = 1
                j=i+1
                while j<len(s):
                    if s[j]=='1':
                        max+=1
                        j+=1
                    else:
                        break
                if max>len_1:
                    len_1=max
                i = j - 1

            else:
                max_0 = 1
                j = i + 1
                while j < len(s):
                    if s[j] == '0':
                        max_0 += 1
                        j += 1
                    else:
                        break
                if max_0 > len_0:
                    len_0 = max_0
                i = j - 1
            i+=1
        return len_1,len_0
        if len_1>len_0:
            return True
        else:
            return False
if __name__=="__main__":
    s = "11100111"
    a=Solution()
    b=a.checkZeroOnes(s)
    print(b)