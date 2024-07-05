class Solution:
    def sortSentence(self, s: str) -> str:
        ls=list(s.split(" "))
        r=[]
        for i in range(len(ls)):
            r.append("")
        for i in range(len(ls)):
            key=int(ls[i][-1])-1
            r[key]=ls[i][0:-1]
        return " ".join(r)

if __name__=="__main__":
    s = "is2 sentence4 This1 a3"
    a=Solution()
    b=a.sortSentence(s)
    print(b)