class Solution:
    def oddString(self, words) -> str:
        ls=[]
        for i in words:
            ls.append('')
        for i in range(len(words[0])-1):
            for j in range(len(words)):
                ls[j]+=str(ord(words[j][i+1])-ord(words[j][i]))
            for j in range(len(ls)):
                if ls.count(ls[j])==1:
                    return words[j]

if __name__=="__main__":
    a=Solution()
    words = ["abm", "bcn", "alm"]
    b=a.oddString(words)
    print(b)