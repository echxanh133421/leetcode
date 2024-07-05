class Solution:
    def find(self, ls, k, index):
        if len(ls) == 1:
            return ls[0]
        else:
            a = k
            while a != 1:
                index += 1
                if index == len(ls):
                    index = 0
                a -= 1
            ls_new = []
            if index == 0:
                ls_new = ls[1:]
            elif index == len(ls) - 1:
                ls_new = ls[:-1]
                index = 0
            else:
                ls_new = ls[0:index] + ls[index + 1:]
            return self.find(ls_new, k, index)

    def findTheWinner(self, n: int, k: int) -> int:
        ls = []
        for i in range(n):
            ls.append(i + 1)

        return self.find(ls, k, 0)

if __name__=='__main__':
    a=Solution()
    n=6
    k=5
    b=a.findTheWinner(n,k)
    print(b)