class Solution:
    def excute(self, start, step, n):
        count = 0
        a = start.copy()
        for i in range(len(step)):
            if step[i] == 'U':
                a[0] -= 1
            elif step[i] == 'D':
                a[0] += 1
            elif step[i] == 'R':
                a[1] += 1
            elif step[i] == 'L':
                a[1] -= 1

            if not (a[0] >= 0 and a[0] <= n - 1) or not (a[1] >= 0 and a[1] <= n - 1):
                break
            count += 1
        return count

    def executeInstructions(self, n: int, startPos, s: str) :
        answer = []
        for i in range(len(s)):
            step_excute = self.excute(startPos, s[i:], n)
            answer.append(step_excute)
        return answer
if __name__=="__main__":
    n =3
    startPos =[0, 1]
    s ="RRDDLU"

    a=Solution()
    b=a.executeInstructions(n,startPos,s)
    print(b)
