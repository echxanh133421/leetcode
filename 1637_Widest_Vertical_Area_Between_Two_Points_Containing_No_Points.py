class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        list_xi_point=[]
        # get xi
        for i in range(len(points)):
            list_xi_point.append(points[i][0])
        #
        list_xi_point.sort()
        max_distance=abs(list_xi_point[0]-list_xi_point[1])
        for i in range(1,len(list_xi_point)-1):
            if abs(list_xi_point[i]-list_xi_point[i+1])>max_distance:
                max_distance=abs(list_xi_point[i]-list_xi_point[i+1])
        return max_distance
