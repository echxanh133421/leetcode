class Solution(object):
    # def min(self,a,b):
    #     if a>=b:
    #         return b
    #     else:
    #         return a
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        for i in range(len(height)-1):
            for j in range(1,len(height)):
                area=(height[i] if height[i]<height[j] else height[j])*(j-i)
                max_area=max(max_area,area)
        return max_area

if __name__=='__main__':
    a=Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(a.maxArea(height))


'''
vẫn chưa đạt yêu cầu
'''
