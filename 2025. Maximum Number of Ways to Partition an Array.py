class Solution:
    def count_number_(self, ls):
        count = 0
        for i in range(1, len(ls)):
            if sum(ls[0:i - 1]) == sum(ls[i:]):
                count += 1
        return count

    def waysToPartition(self, nums, k):
        number_of_ls = len(nums) + 1
        ls_count = []

        for i in range(0, number_of_ls):
            # so luong cac chuoi can tinh
            if i == len(nums):
                ls_num = nums.copy()
            else:
                ls_num = nums.copy()
                ls_num[i] = k

            # tinh toan
            ls_count.append(self.count_number_(ls_num))
        return max(ls_count)

if __name__=="__main__":
    # ls=[22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14]
    a=Solution()
    k=-33
    # b=a.waysToPartition(ls,k)
    # print(b)
    ls1=[22, 4, -33, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14]
    c,ls2=a.count_number_(ls1)
    print(c)
    print(ls2)

    '''chua giai quyet được'''