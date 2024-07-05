class Solution:
    def findMaxLength(self, nums) :
        l=len(nums)
        if l<=1:
            return 0
        elif nums.count(0)==nums.count(1):
            return l
        else:
            if l%2==0:
                l1=self.findMaxLength(nums[0:l-2])
                l2=self.findMaxLength(nums[2:l])
                l3=self.findMaxLength(nums[1:l-1])
                return max(l1,l2,l3)
            else:
                l1=self.findMaxLength(nums[:l-1])
                l2=self.findMaxLength(nums[1:l])
                return max(l1,l2)

if __name__=="__main__":
    a=Solution()
    nums=[0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
    b=a.findMaxLength(nums)
    print(b)
    '''chua gia quyet duoc'''