class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        str_b=''
        while n!=0:
            str_b+=str(n%2)
            n=int(n/2)
        str_f=''
        for i in range(len(str_b)-1,-1,-1):
            if str_b[i]=='1':
                str_f+='0'
            else:
                str_f+='1'
        num=0
        j=0
        for i in range(len(str_f)-1,-1,-1):
            num+=int(str_f[i])*(2**j)
            j+=1
        return num
if __name__=='__main__':
    n=0
    a=Solution()
    b=a.bitwiseComplement(n)
    print(b)