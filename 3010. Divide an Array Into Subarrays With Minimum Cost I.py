class Solution:
    def minimumCost(self, nums) -> int:
        a=min(nums[1:])
        index=0
        for i in range(1,len(nums)):
            if nums[i]==a:
                index=i
                break
        if index==len(nums)-1:
            b=min(nums[1:index])
            return nums[0]+a+b
        elif index==1:
            b=min(nums[index+1:])
            return nums[0]+a+b
        else:
            b=min(nums[1:index])
            c=min(nums[index+1:])
            d=min(b,c)
            return nums[0]+a+d
if __name__=="__main__":
    nums = [1, 2, 3, 12]
    a=Solution()
    b=a.minimumCost(nums)
    print(b)