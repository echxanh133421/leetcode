class Solution:
    def plusOne(self, digit) :
        self.digits_result=digit.copy()
        i=len(digit)
        if (self.digits_result[i-1]!=9):
            self.digits_result[i-1]+=1

        else:
            while(self.digits_result[i-1]==9 and i-1>0):
                self.digits_result[i - 1] = 0
                i-=1
            self.digits_result[i-1]+=1
        if(digit[0]==9 and self.digits_result[0]==10):
            self.digits_result[0:1]=[1,0]
        return self.digits_result


if __name__=="__main__":
    A=Solution()
    print(A.plusOne([9,9]))