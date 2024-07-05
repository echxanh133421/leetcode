class Solution:
    def check_prime(self, n):
        a=int(n**(1/2))+1
        for i in range(2,a ):
            if n % i == 0:
                return True
        return False

    def smallestValue(self, n: int) -> int:

        a = n

        while self.check_prime(a):
            ls = []
            i = 2
            b=a
            while a!=1:
                while a%i==0:
                    ls.append(i)
                    a=int(a/i)
                i+=1
            if sum(ls)>=b:
                return b
            else:
                a=sum(ls)
        return a


if __name__=="__main__":
    a=Solution()
    n=15
    b=a.smallestValue(n)
    print(b)