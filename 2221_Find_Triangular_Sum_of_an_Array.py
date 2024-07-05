class Solution:
    def triangularSum(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            list_sub=[]
            for i in range(len(nums)-1):
                list_sub.append(nums[i]+nums[i+1])
            return(self.triangularSum(list_sub))

A=Solution()
print(A.triangularSum([1,2,3,4,5]))