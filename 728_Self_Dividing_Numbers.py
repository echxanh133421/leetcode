class Solution:
    def check(self,num):
        ls_num_container=list(str(num))
        c=True
        for i in range(len(ls_num_container)):
            if ls_num_container[i]=='0':
                return False
            else:
                if num%int(ls_num_container[i])!=0:
                    return False
        return c
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ls_final=[]
        for i in range(left,right+1):
            if self.check(i):
                ls_final.append(i)
        return ls_final
