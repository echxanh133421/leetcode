class Solution:
    def numberOfBeams(self, bank) -> int:
        item=len(bank[0])
        for i in range(len(bank)-1):
            if bank[i]=="0"*item:
                bank[i:]=bank[i+1:]
        sum_=0
        for i in range(len(bank)-1):
            for j in bank[i]:
                if j=='1':
                    for k in bank[i+1]:
                        if k=='1':
                            sum_+=1
        return sum_
if __name__=="__main__":
    bank = ["011001", "000000", "010100", "001000"]
    a=Solution()
    print(a.numberOfBeams(bank))
    'chua giai duoc'