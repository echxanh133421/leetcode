class Solution:
    # max item in cols j
    def max_col(self, grid, j):
        max = grid[0][j]
        for i in range(len(grid)):
            if max < grid[i][j]:
                max = grid[i][j]
        return max

    def maxIncreaseKeepingSkyline(self, grid) -> int:
        # create matrix arr
        arr=[]
        cols = len(grid)
        rows = len(grid)
        for i in range(rows):
            arr_row=[]
            for j in range(cols):
                arr_row.append(grid[i][j])
            arr.append(arr_row)

        # main algorithm
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < max(grid[i]) and grid[i][j] < self.max_col(grid, j):
                    if max(grid[i]) < self.max_col(grid, j):
                        arr[i][j] = max(grid[i])
                    else:
                        arr[i][j] = self.max_col(grid, j)
                else:
                    arr[i][j] = grid[i][j]
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum = sum + arr[i][j] - grid[i][j]
        return sum


if __name__=="__main__":
    grid=[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    A=Solution()
    b=A.maxIncreaseKeepingSkyline(grid)
    print(b)
