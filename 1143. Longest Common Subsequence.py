class Solution:
    def max_sub(self, s1, s2):
        i = 0
        count = 0
        while i < len(s1) and i < len(s2):
            if s1[i] == s2[i]:
                count += 1
                i += 1
            else:
                return count

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        max_substr = 0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text2[j] == text1[i]:
                    a = self.max_sub(text1[i:], text2[j:])
                else:
                    a=0

                if a > max_substr:
                    max_substr = a
        return max_substr

if __name__=="__main__":
    text1 = "abcde"
    text2 = "ace"
    a=Solution()
    b=a.longestCommonSubsequence(text1,text2)
    print(b)

    '''chua gia duoc'''