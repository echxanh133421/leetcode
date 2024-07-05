class Solution:
    def countAsterisks(self, s: str) -> int:
        if '|' not in s:
            return 0
        else:
            count=0
            i=0
            count_star=0
            while i<len(s):
                if count%2==0:
                    if s[i]=="*":
                        count_star+=1
                    elif s[i]=='|':
                        count+=1
                    i+=1
                else:
                    if s[i]=="|":
                        count+=1
                    i+=1
            return count_star
if __name__=="__main__":
    s ="l|*e*et|c**o|*de|"
    a=Solution()
    print(a.countAsterisks(s))