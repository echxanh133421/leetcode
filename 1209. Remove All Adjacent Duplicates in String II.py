class Solution:
    def check(self,stack,s):
        if stack==s*len(stack):
            return True
        return False
    def removeDuplicates(self, s: str, k: int) -> str:
        i=0
        stack=''
        while i<len(s):
            if len(stack)<k-1:
                stack+=s[i]
            else:
                if self.check(stack[-(k-1):],s[i]):
                    stack=stack[:-k+1]
                else:
                    stack+=s[i]
            i+=1
        return stack

if __name__=="__main__":
    a=Solution()
    s = "deeedbbcccbdaa"
    k = 3
    b=a.removeDuplicates(s,k)
    print(b)