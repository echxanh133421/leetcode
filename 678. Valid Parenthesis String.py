class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0


if __name__=="__main__":
    s="(((((()*)(*)*))())())(()())())))((**)))))(()())()"
    #s='('
    a=Solution()
    b=a.checkValidString(s)
    #print(b[0])
    #print(b[1])
    print(b)
