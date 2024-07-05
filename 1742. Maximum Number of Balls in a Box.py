class Solution:
    def sum_num_in_id_ball(self, a):
        b = list(str(a))
        sum = 0
        for i in range(len(b)):
            sum += int(b[i])
        return sum

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        min = self.sum_num_in_id_ball(lowLimit)
        max = min
        for i in range(lowLimit + 1, highLimit + 1):
            a=self.sum_num_in_id_ball(i)
            if a < min:
                min = a
            if a > max:
                max = a
        ls = []
        for i in range(min, max + 1):
            ls.append(0)

        for i in range(lowLimit, highLimit + 1):
            ls[self.sum_num_in_id_ball(i) - min] += 1

        max_ball=ls[0]
        for i in range(1,len(ls)):
            if ls[i]>max_ball:
                max_ball=ls[i]
        return max_ball
if __name__=="__main__":
    a=Solution()
    lowLimit = 1
    highLimit = 10
    b=a.countBalls(lowLimit,highLimit)
    print(b)