class Solution:
    def largestAltitude(self, gain) -> int:
        altitude=[]
        start=0
        altitude.append(start)
        for i in range(len(gain)):
            start+=gain[i]
            altitude.append(start)
        return max(altitude)

if __name__=="__main__":
    gain =[-4, -3, -2, -1, 4, 3, 2]
    A=Solution()
    print(A.largestAltitude(gain))