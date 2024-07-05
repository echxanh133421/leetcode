class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        leng=len(arr)
        odd_int=leng-1 if leng%2==0 else leng
        result=sum(arr)
        for i in range(3,odd_int+1,2): #số lượng phần tử trong mảng con
            for j in range(0,leng):#start index
                if j+i>leng:
                    break
                else:
                    result+=sum(arr[j:j+i])
        return result

if __name__=="__main__":
    arr =[1, 4, 2, 5, 3]
    A=Solution()
    b=A.sumOddLengthSubarrays(arr)
    print(b)