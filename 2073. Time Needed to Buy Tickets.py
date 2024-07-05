class Solution:
    def timeRequiredToBuy(self, tickets, k: int) -> int:
        count=0
        a=tickets[k]-1
        count=a*len(tickets)
        for i in range(len(tickets)):
            tickets[i]-=a
        for i in range(0,k+1):
            tickets[i]-=1
            count+=1
        for i in range(len(tickets)):
            if tickets[i]<0:
                count+=tickets[i]
        return count
if __name__=="__main__":
    k=0
    tickets=[5,1,1,1]
    a=Solution()
    b=a.timeRequiredToBuy(tickets,k)
    print(b)