class Solution:
    def addDigits(self, num: int) -> int:
        if len(list(str(num)))==1:
            return num
        else:
            sum=0
            a=list(str(num))
            for i in range(len(a)):
                sum+=int(a[i])
            return self.addDigits(sum)

if __name__=="__main__":
    A=Solution()
    b=A.addDigits(38)
    print(b)