class Solution:
    def check(self,a,b):
        m=min(a,b)
        count=0
        for i in range(2,m+1):
            if a%i==0 and b%i==0:
                return False
        return True
    def countBeautifulPairs(self, nums) -> int:
        ls=[]
        nums1=[]
        for i in range(len(nums)):
            nums1.append(int(nums[i]%10))
        for i in range(0,len(nums1)-1):
            a = nums1[i]
            for j in range(i+1,len(nums1)):
                b=nums1[j]
                if self.check(a,b):
                    if ls==[]:
                        ls.append([a,b])
                    else:
                        check=False
                        for i in range(len(ls)):
                            if ls[i][0]==a and ls[i][1]==b:
                                check=True
                                break
                        if check:
                            pass
                        else:
                            ls.append([a,b])
        return len(ls)
if __name__=="__main__":
    a=Solution()
    num=[31,25,72,79,74]
    b=a.countBeautifulPairs(num)
    print(b)
    '''chua giai duoc'''