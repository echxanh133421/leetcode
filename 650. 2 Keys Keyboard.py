class Solution:
    def prime(self,n):
        for i in range(2,int(n**(1/2))+1):
            if n%i==0:
                return True
        return False
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        elif not self.prime(n):
            return n
        else:
            if n%2==0:
                return 2+self.minSteps(int(n/2))
            else:

                ls = []
                i = n-1
                a=n
                while True:
                    if a%i==0:
                        break
                    i-=1
                return self.minSteps(i)+(int(n/i)-1)+1

if __name__=="__main__":
    a=Solution()
    n=9
    b=a.minSteps(n)
    print(b)


