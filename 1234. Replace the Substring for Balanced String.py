class Solution:
    def check(self, q, w, e, r, n):
        quater = int(n / 4)
        if q == quater and w == quater and e == quater and r == quater:
            return True
        else:
            return False

    def balancedString(self, s: str) :
        ls = [0, 0, 0, 0]
        for i in range(len(s)):
            if s[i] == 'Q':
                ls[0] += 1
            elif s[i] == 'W':
                ls[1] += 1
            elif s[i] == 'E':
                ls[2] += 1
            else:
                ls[3] += 1
        n = len(s)
        return ls


if __name__=="__main__":
    a=Solution()
    s="WWWEQRQEWWQQQWQQQWEWEEWRRRRRWWQE"
    b=a.balancedString(s)
    print(b)
    '''chua lam duoc'''