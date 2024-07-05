class Solution:
    def closetTarget(self, words, target, startIndex) -> int:
        if target not in words:
            return -1
        else:
            left_run=0
            right_run=0
            startIndex1=startIndex
            while True:
                if startIndex1<=len(words)-1:
                    if words[startIndex1]==target:
                        break
                    else:
                        startIndex1+=1
                        right_run+=1
                else:
                    startIndex1=0
            while True:
                if startIndex>=0:
                    if words[startIndex]==target:
                        break
                    else:
                        startIndex-=1
                        left_run+=1
                else:
                    startIndex=len(words)-1
            return min(left_run,right_run)
if __name__=='__main__':
    a=Solution()
    words =["hello", "i", "am", "leetcode", "hello"]
    startIndex=1
    target='hello'
    b=a.closetTarget(words,target,startIndex)
    print(b)