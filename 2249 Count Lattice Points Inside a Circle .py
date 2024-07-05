class Solution:
    def check_in_circle(self,i,j,circle):
        if pow(i-circle[0],2)+pow(j-circle[1],2)<=pow(circle[2],2):
            return True
        else:
            return False
    def node_in_circles(self,circle):
        startx=circle[0]-circle[2]
        endx=circle[0]+circle[2]
        starty=circle[1]-circle[2]
        endy=circle[1]+circle[2]

        ls=[]
        for i in range(startx,endx+1):
            for j in range(starty,endy+1):
                if self.check_in_circle(i,j,circle):
                    ls.append(str(i)+","+str(j))
        return ls

    def countLatticePoints(self, circles) -> int:
        ls=[]
        for i in range(len(circles)):
            ls+=self.node_in_circles(circles[i])
        return len(set(ls))

if __name__=="__main__":
    circles = [[6, 4, 1], [2, 7, 1], [6, 4, 4], [8, 4, 4], [10, 9, 6], [1, 9, 1], [3, 3, 2], [4, 7, 2], [6, 4, 2],
                [2, 10, 2], [7, 5, 5], [10, 4, 2], [8, 6, 4], [3, 2, 2], [2, 2, 1], [5, 4, 4], [6, 7, 5], [10, 1, 1]]
    a= Solution()
    b=a.countLatticePoints(circles)
    print(b)

