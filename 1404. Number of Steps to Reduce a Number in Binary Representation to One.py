class Solution:
    def numSteps(self, s: str):
        a=len(s)
        num=0
        for i in range(len(s)):
            if s[i] == '1':
                num += (2 ** (a - 1))
            a -= 1
        step=0
        while num!=1:
            if num%2==0:
                num=int(num/2)
            else:
                num+=1
            step+=1
        return step

a=Solution()
s="1111011110000011100000110001011011110010111001010111110001"
b=a.numSteps(s)
print(b)