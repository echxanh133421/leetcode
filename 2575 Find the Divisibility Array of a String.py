class Solution:
    def divisibilityArray(self, word: str, m: int):
        ls=[]
        for i in range(len(word)):
            a=int(word[:i+1])
            if a %m==0:
                ls.append(1)
            else:
                ls.append(0)
        return ls

if __name__=="__main__":
    word = "998244353"
    m = 3
    a=Solution()
    print(a.divisibilityArray(word,m))