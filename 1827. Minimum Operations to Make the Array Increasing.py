class Solution:
    def minOperations(self, nums) -> int:
        i=0
        count=0
        while i<len(nums)-1:
            if nums[i+1]<=nums[i]:

                count=count+nums[i]-nums[i+1]+1
                nums[i + 1] = nums[i] + 1
            i+=1
        return count
if __name__=="__main__":
    a=Solution()
    nums=[1,1,1]
    b=a.minOperations(nums)
    print(b)