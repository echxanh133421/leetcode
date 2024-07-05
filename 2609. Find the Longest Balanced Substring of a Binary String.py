class Solution:
    def find_min_str(self,s):
        a=s.count('0')
        b=len(s)-a
        return min(a,b)
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ls=[]
        pivot=0
        for i in range(len(s)):
            if i<len(s)-1:
                if (s[i] == '1' and s[i + 1] == '0'):
                    ls.append(s[pivot:i + 1])
                    pivot = i + 1
            else:
                if(s[i]=='1' and i==len(s)-1):
                    ls.append(s[pivot:i+1])
                    pivot=i+1
        if ls==[]:
            return 0
        max=self.find_min_str(ls[0])
        for i in range(len(ls)):
            if self.find_min_str(ls[i])>max:
                max=self.find_min_str(ls[i])
        return max
if __name__=="__main__":
    s='01000111'
    a=Solution()
    b=a.findTheLongestBalancedSubstring(s)
    print(b)