class Solution:
    def findSpecialInteger(self, arr) -> int:
        l=len(arr)
        ls=[]
        ls1=[]
        count=1
        i=0
        while i<l:
            if i==l-1:
                ls.append(count)
                ls1.append(arr[i])
                break
            else:
                if arr[i]==arr[i+1]:
                    count+=1
                    i+=1
                else:
                    ls.append(count)
                    ls1.append(arr[i])
                    count=1
                    i+=1
        return ls1[ls.index(max(ls))]
if __name__=="__main__":
    ls=[1,2,2,6,6,6,6,7,10]
    a=Solution()
    b=a.findSpecialInteger(ls)
    print(b)