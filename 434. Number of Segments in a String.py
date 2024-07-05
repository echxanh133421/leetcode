class Solution:
    def countSegments(self, s: str) -> int:
        if s == '':
            return 0
        else:
            count = 0
            i = 0
            while i < len(s):
                if s[i] == ' ':
                    pass
                else:
                    j = i
                    while s[j]!=' ' and j < len(s):
                        j = j + 1
                        if j>len(s)-1:
                            return count+1
                    count += 1
                    i=j
                    if i==len(s):
                        break
                i += 1

            return count

if __name__=="__main__":
    a=Solution()
    s="Hello, my name is John"
    b=a.countSegments(s)
    print(b)