class Solution:
    def isPossibleDivide(self, nums, k: int) -> bool:
        if len(nums)%k!=0:
            return False
        else:
            if k==1:
                return True
            else:
                a=nums.copy()
                while a!=[]:
                    start=min(a)
                    a.remove(start)
                    for i in range(1,k):
                        if start+1 in a:
                            a.remove(start+1)
                            start=start+1
                        else:
                            return False
                return True
if __name__=='__main__':
    nums=[1,2,3,3,4,4,5,6]
    k=4
    a=Solution()
    b=a.isPossibleDivide(nums,k)
    print(b)
    '''time limited'''