class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l=[]
        u=[]
        for i in range(len(word)):
            if ord(word[i])>=97 and ord(word[i])<=122 and word[i] not in l:
                l.append(word[i])
            elif ord(word[i])>=65 and ord(word[i])<=90 and word[i] not in u:
                u.append(word[i])

        count=0
        for i in range(len(l)):
            if l[i].upper() in u:
                count+=1
        return count

if __name__=="__main__":
    word = "aaAbcBC"
    a=Solution()
    b=a.numberOfSpecialChars(word)
    print(b)