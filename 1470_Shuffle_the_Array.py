class Solution:
    def shuffle(self, nums, n: int):
        list_final=[]
        j=0
        k=n
        for i in range(2*n):
            if i%2==0:
                list_final.append(nums[j])
                j+=1
            else:
                list_final.append(nums[k])
                k+=1
        return list_final

if __name__=="__main__":
    A=Solution()
    ls=[1,2,3,4,4,3,2,1]
    n = 4
    print(A.shuffle(ls,n))