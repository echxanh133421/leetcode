class Solution:
    def averageWaitingTime(self, customers) -> float:
        if len(customers)==1:
            return customers[0][1]
        current=customers[0][0]+customers[0][1]
        sum_wait=customers[0][1]
        for i in range(1,len(customers)):
            if current>=customers[i][0]:
                current+=customers[i][1]
                sum_wait+=current-customers[i][0]
            else:
                current=customers[i][0]+customers[i][1]
                sum_wait+=customers[i][1]
        return sum_wait/len(customers)
if __name__=='__main__':
    customers=[[1, 2], [2, 5], [4, 3]]
    a=Solution()
    b=a.averageWaitingTime(customers)