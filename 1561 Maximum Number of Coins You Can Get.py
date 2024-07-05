class Solution:
    def maxCoins(self, piles) -> int:
        for i in range(len(piles)-1):
            for j in range(i+1,len(piles)):
                if piles[i]<piles[j]:
                    swap=piles[i]
                    piles[i]=piles[j]
                    piles[j]=swap
        sum=0
        for i in range(1,len(piles),3):
            sum+=piles[i]
        return sum
if __name__=="__main__":
    piles =[9, 8, 7, 6, 5, 1, 2, 3, 4]
    a=Solution()
    print(a.maxCoins(piles))
    '''chua giai duoc'''