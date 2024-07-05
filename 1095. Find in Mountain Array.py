class MountainArray:
    def __init__(self,arr):
        self.arr=arr
    def get(self, index: int) -> int:
        return self.arr[index]
    def length(self) -> int:
        return len(self.arr)

class Solution:
    def peakIndexInMountainArray(self, mountain_arr, left, right):

        if right - left + 1 == 3:
            return 1
        else:
            mid = int((left + right) / 2)
            if mountain_arr.get(mid) > mountain_arr.get(mid - 1) and mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                return mid
            elif mountain_arr.get(mid) < mountain_arr.get(mid - 1):
                return self.peakIndexInMountainArray(mountain_arr, left, mid)
            else:
                return self.peakIndexInMountainArray(mountain_arr, mid, right)

    def binary_search1(self, mountain_arr, left, right, target):
        mid = int((left + right) / 2)
        if mountain_arr.get(mid) == target:
            return mid
        else:
            if left == right:
                return -1
            else:
                if mountain_arr.get(mid) < target:
                    self.binary_search1(mountain_arr, mid + 1, right, target)
                else:
                    self.binary_search1(mountain_arr, left, mid - 1, target)

    def binary_search2(self, mountain_arr, left, right, target):
        mid = int((left + right) / 2)
        if mountain_arr.get(mid) == target:
            return mid
        else:
            if left == right:
                return -1
            else:
                if mountain_arr.get(mid) > target:
                    self.binary_search2(mountain_arr, mid + 1, right, target)
                else:
                    self.binary_search2(mountain_arr, left, mid - 1, target)

    def findInMountainArray(self, target: int, mountain_arr) -> int:
        right = mountain_arr.length() - 1
        left = 0
        mid_find = self.peakIndexInMountainArray(mountain_arr, left, right)


        # find_left = self.binary_search1(mountain_arr, left, mid_find, target)
        # find_right = self.binary_search2(mountain_arr, mid_find + 1, right, target)

        # if find_left != -11:
        #     return find_left
        # else:
        #     if find_right == -1:
        #         return -1
        #     else:
        #         return find_right
        if mid_find>int((right+left)/2):
            find_left = self.binary_search1(mountain_arr, left, mid_find, target)
            find_right=-1
            for i in range(mid_find+1,right+1):
                if mountain_arr.get(i)==target:
                    find_right=i
                    break
        else:
            find_left=-1
            for i in range(left,mid_find+1):
                if mountain_arr.get(i)==target:
                    find_left=i
                    break
            find_right = self.binary_search2(mountain_arr, mid_find + 1, right, target)

        if find_left != -1:
            return find_left
        else:
            if find_right == -1:
                return -1
            else:
                return find_right

if __name__=="__main__":
    array = [0,1,2,4,2,1]
    target = 3
    arr_mou=MountainArray(array)
    a=Solution()
    b=a.findInMountainArray(target,arr_mou)
    print(b)
    '''chưa giải được'''