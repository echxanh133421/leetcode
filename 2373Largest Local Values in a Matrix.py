class Solution:
    def max(self,grid,row,col):
        max_=grid[row][col]
        for i in range(row,row+3):
            for j in range(col,col+3):
                if grid[i][j]>max_:
                    max_=grid[i][j]
        return max_

    def largestLocal(self, grid):
        n = len(grid)
        grid_out = []
        for i in range(n - 2):
            ls = []
            for j in range(n - 2):
                ls.append(0)
            grid_out.append(ls)

        for i in range(n - 2):
            for j in range(n - 2):
                grid_out[i][j] = self.max(grid,i,j)
        return grid_out

if __name__=="__main__":
    grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    a=Solution()
    b=a.largestLocal(grid)
    print(b)