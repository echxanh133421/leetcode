class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_b = blocks[0:k].count('B')
        index_max = 0
        for i in range(1, len(blocks) - k+1):
            if blocks[i:k + i].count('B') > max_b:
                max_b = blocks[i:k + i].count('B')
                index_max = i

        return k - max_b

if __name__=="__main__":
    s="WWBBBWBBBBBWWBWWWB"
    k=16
    a=Solution()
    print(len(s))
    print(a.minimumRecolors(s,k))
