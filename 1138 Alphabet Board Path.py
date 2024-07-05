class Solution:
    def get_pos(self, char):
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        pos = []
        for i in range(len(board)):
            if char in board[i]:
                pos.append(i)
                for j in range(len(board[i])):
                    if board[i][j] == char:
                        pos.append(j)
                        return pos

    def alphabetBoardPath(self, target: str) -> str:

        start_point = [0, 0]
        ls_final = ''
        for i in range(len(target)):
            if target[i]!='z':
                a = self.get_pos(target[i])
                if a[0] == start_point[0] and a[1] == start_point[1]:
                    ls_final += '!'
                else:
                    if a[0] > start_point[0]:
                        ls_final += 'D' * (a[0] - start_point[0])
                    elif a[0] < start_point[0]:
                        ls_final += 'U' * (-a[0] + start_point[0])

                    if a[1] > start_point[1]:
                        ls_final += 'R' * (a[1] - start_point[1])
                    elif a[1] < start_point[1]:
                        ls_final += 'L' * (-a[1] + start_point[1])

                    ls_final += '!'

            else:
                a=[5,0]
                if start_point==a:
                    ls_final+='!'
                else:
                    if start_point[1]==0:
                        ls_final+='D'*(a[0]-start_point[0])
                    else:
                        ls_final += 'D' * (a[0] - start_point[0]-1)
                        ls_final+='L'* start_point[1]
                        ls_final+='D'
                    ls_final+='!'
            start_point[0] = a[0]
            start_point[1] = a[1]
        return ls_final

if __name__=="__main__":
    target = "leet"
    a=Solution()
    b=a.alphabetBoardPath(target)
    print(b)