class Solution:
    def addBinary(self, a, b):
        i=len(a)
        j=len(b)
        remeber='0'
        final_str=[]
        while(i>=1 and j>=1):
            sum=int(a[i-1])+int(b[j-1])+int(remeber)
            if sum==0 or sum==1:
                final_str.append(sum)
                remeber='0'
            else:
                remeber='1'
                if sum==2:
                    final_str.append(0)
                else:
                    final_str.append(1)
            i-=1
            j-=1
        while(i>=1):
            sum = int(a[i - 1]) + int(remeber)
            if sum==1 or sum==0:
                final_str.append(sum)
                remeber='0'
            else:
                remeber='1'
                final_str.append(0)
            i-=1
        while (j >= 1):
            sum = int(b[j - 1]) + int(remeber)
            if sum == 1 or sum == 0:
                final_str.append(sum)
                remeber='0'
            else:
                remeber = '1'
                final_str.append(0)
            j-=1
        if remeber=='1':
            final_str.append(1)
        final_str.reverse()

        return ''.join(str(e) for e in final_str)
if __name__=="__main__":
    A=Solution()
    a='1010'
    b='1011'
    B=A.addBinary(a,b)
    print(B)