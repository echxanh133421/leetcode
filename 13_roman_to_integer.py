
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000
            }
        list_number=[]
        for i in s:
            for x in dic:
                if i==x:
                    list_number.append(dic.get(x))
        print(list_number)
        sum=0          
        for x in range(len(list_number)-1):
            if list_number[x]<list_number[x+1]:
                sum=sum-list_number[x]
            else:
                sum+=list_number[x]
        sum+=list_number[len(list_number)-1]

        return sum
            


if __name__=='__main__':

        a = Solution()
        print(a.romanToInt(input()))
