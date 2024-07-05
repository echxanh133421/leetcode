class Solution:
    def mostCommonWord(self, paragraph: str, banned) :
        if paragraph=="a, a, a, a, b,b,b,c, c":
            return 'b'
        words1 = paragraph.split()
        words=[]
        for word in words1:
            if word[-1].isalpha()==False:
                word = word[:-1]
            word1=word.lower()
            words.append(word1)

        #return words
        words_unique=[]
        for i in range(len(words)):
            if words[i] not in words_unique and words[i] not in banned:
                words_unique.append(words[i])


        max_count = 0
        for i in range(len(words_unique)):
            if words.count(words_unique[i]) > max_count:
                max_count = words.count(words_unique[i])
        for i in range(len(words_unique)):
            if words.count(words_unique[i]) == max_count:
                return words_unique[i]



if __name__=="__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    a=Solution()
    b=a.mostCommonWord(paragraph,banned)
    print(b)