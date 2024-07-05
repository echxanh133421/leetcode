class Solution:
    def dayOfYear(self, date: str) -> int:
        ls=list(date.split('-'))
        ls1=[31,28,31,30,31,30,31,31,30,31,30,31]
        ls2=[31,29,31,30,31,30,31,31,30,31,30,31]

        day_th=0
        if int(ls[0])%4!=0:
            if int(ls[1]) == 1:
                return int(ls[2])
            else:
                for i in range(1, int(ls[1])):
                    day_th += ls1[i-1]
                return day_th + int(ls[2])
        else:
            if int(ls[1])==1:
                return int(ls[2])
            else:
                for i in range(1,int(ls[1])):
                    day_th+=ls2[i-1]
                return day_th+int(ls[2])

if __name__=="__main__":
    date="1900-05-02"
    a=Solution()
    print(a.dayOfYear(date))