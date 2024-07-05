class Solution:
    def furthestDistanceFromOrigin(self, moves: str):
        l=0
        r=0
        a=0
        for i in moves:
            if i=='R':
                r+=1
            elif i=='L':
                l+=1
            else:
                a+=1
        if l>=r:
            return a+l-r
        else:
            return a+r-l


if __name__=="__main__":
    a=Solution()
    moves = "_R__LL_"
    b=a.furthestDistanceFromOrigin(moves)
    print(b)