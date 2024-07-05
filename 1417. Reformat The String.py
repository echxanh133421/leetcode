class Solution:
    def reformat(self, s: str) -> str:
        number = []
        string = []
        for i in range(len(s)):
            if s[i].isdigit():
                number.append(s[i])
            else:
                string.append(s[i])
        if abs(len(string) - len(number)) >= 2:
            return ''
        else:
            i = 0
            j = 0
            s_final = ''
            if len(number) > len(string):
                while i < len(number) and j < len(string):
                    s_final += number[i]
                    s_final += string[j]
                    i += 1
                    j += 1

                s_final += number[i]
            elif len(number) < len(string):
                while i < len(number) and j < len(string):
                    s_final += number[i]
                    s_final += string[j]
                    i += 1
                    j += 1
                s_final += string[j]
            else:
                if
            return s_final
if __name__=="__main__":
    a=Solution()
    s="a0b1c2"
    b=a.reformat(s)
    print(b)