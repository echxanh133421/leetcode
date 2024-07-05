class Solution:
    def removeKdigits(self, num, k) :
        if k==len(num):
            return '0'
        ls_digit=num
        i=0
        # while k!=0:
        #     if i<len(ls_digit)-1:
        #         if int(ls_digit[i])<int(ls_digit[i+1]):
        #             a=ls_digit[:i+1]
        #             b=ls_digit[i+2:]
        #             ls_digit=a+b
        #             k-=1
        #         elif int(ls_digit[i])>int(ls_digit[i+1]):
        #             a = ls_digit[:i]
        #             b = ls_digit[i+1:]
        #             ls_digit = a + b
        #             k -= 1
        #         else:
        #             i+=1
        #     else:
        #         i=0
        #     if len(list(set(ls_digit)))==1:
        #         a=[ls_digit[0]]
        #         l=len(ls_digit)
        #         ls_digit=a*(l-k)
        #         break
        while k!=0:
            if i<len(ls_digit)-1:
                if int(ls_digit[i])<=int(ls_digit[i+1]):
                    i+=1
                elif int(ls_digit[i])>int(ls_digit[i+1]):
                    a = ls_digit[:i]
                    b = ls_digit[i+1:]
                    ls_digit = a + b
                    k -= 1
            elif i==len(ls_digit)-1:
                if ls_digit[i]!='0':
                    ls_digit = ls_digit[:-1]
                    k -= 1
                else:
                    i+=1
            else:
                i=0
            if len(list(set(ls_digit))) == 1:
                a = ls_digit[0]
                l = len(ls_digit)
                ls_digit = a * (l - k)
                break
        if ls_digit[0]!='0':
            return ls_digit
        i=0
        while ls_digit[i]=='0':
            i+=1
        return ls_digit[i:]

if __name__=="__main__":
    num = "10200"
    k = 1
    a=Solution()
    b=a.removeKdigits(num,k)
    print(b)
    '''chua giai duoc'''