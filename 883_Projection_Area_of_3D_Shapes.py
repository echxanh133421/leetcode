class Solution:
    def projectionArea(self, grid) -> int:

        x=0
        z=0
        y=0

        for i in range(len(grid)):
            z+=max(grid[i])
        for i in range(len(grid)):
            m=0
            for j in range(len(grid[0])):
                if grid[j][i]>m:
                    m=grid[j][i]
                if grid[i][j]!=0:
                    x+=1
            y+=m
        return x+y+z
        pass


if __name__=="__main__":
    grid=[[1,0],[5,4]]
    A=Solution()
    b=A.projectionArea(grid)
    print(b)