class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        list1=list(num1)
        list2=list(num2)
        list3=[]
        i=len(list1)-1
        j=len(list2)-1
        remember=0
        while i>=0 or j>=0:
            if i==-1 and j!=-1:
                a=int(num2[j])+remember
                j-=1
            elif j==-1 and i!=-1:
                a=int(num1[i])+remember
                i-=1
            else:
                a=int(num1[i])+int(num2[j])+remember
                i-=1
                j-=1
            if a>=10:
                remember=1
                list3.append(str(a%10))
            else:
                remember=0
                list3.append(str(a))
        if remember==1:
            list3.append(str(remember))
        list3.reverse()
        return ''.join(list3)

if __name__=="__main__":
    A=Solution()
    num1='11'
    num2='123'
    print(A.addStrings(num1,num2))

