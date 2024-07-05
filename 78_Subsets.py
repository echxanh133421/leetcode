class Solution:
    def subsets(self, nums):
        list_final=[[],]
        for i in range(1,len(nums)+1):
            for j in range(i+1,len(nums)):
                pass

        list_final.append(nums)
        return list_final

if __name__=="__main__":
    A=Solution()
    nums = [1, 2, 3]
    print(A.subsets(nums))
    '''chua giai quyet dc'''
