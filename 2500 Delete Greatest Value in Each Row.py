class Solution:
    def deleteGreatestValue(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0]) - 1):
                for k in range(j + 1, len(grid[0])):
                    if grid[i][j] > grid[i][k]:
                        swap = grid[i][j]
                        grid[i][j] = grid[i][k]
                        grid[i][k] = swap

        answer = 0
        for i in range(len(grid[0])):
            max = grid[0][i]
            for j in range(len(grid)):
                if grid[j][i] > max:
                    max = grid[j][i]
            answer += max
        return answer

if __name__=="__main__":
    grid=[[1,2,4],[3,3,1]]
    a=Solution()
    b=a.deleteGreatestValue(grid)
    print(b)