class Solution:
    def matrixScore(self, grid) :
        for i in range(len(grid)):
            if grid[i][0]==0:
                for j in range(len(grid[i])):
                    a=1-grid[i][j]
                    grid[i][j]=a
        ls=[]
        for i in range(len(grid[0])):
            ls_sub=[]
            for j in range(len(grid)):
                ls_sub.append(grid[j][i])
            ls.append(ls_sub)

        for i in range(len(ls)):
            count_1=ls[i].count(1)
            count_0=ls[i].count(0)
            if count_1<count_0:
                for j in range(len(ls[i])):
                    a=1-ls[i][j]
                    ls[i][j]=a

        ls1 = []
        for i in range(len(ls[0])):
            ls_sub = []
            for j in range(len(ls)):
                ls_sub.append(ls[j][i])
            ls1.append(ls_sub)

        sum=0
        for i in range(len(ls1)):
            str_=''
            for j in range(len(ls1[0])):
                str_+=str(ls1[i][j])
            sum+=int(str_, 2)
        return sum

if __name__=="__main__":
    grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    a=Solution()
    b=a.matrixScore(grid)
    print(b)
