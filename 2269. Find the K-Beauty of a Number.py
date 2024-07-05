class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num=str(num)
        count=0
        for i in range(len(str_num)-k+1):
            a=int(str_num[i:i+k])
            if a==0:
                continue
            if num%a==0:
                count+=1
        return count

if __name__=="__main__":
    num=30003
    k=3
    a=Solution()
    b=a.divisorSubstrings(num,k)
    print(b)