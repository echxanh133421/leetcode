class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1=nums1
        self.nums2=nums2

    def add(self, index: int, val: int) -> None:
        # a=self.nums2[index:].copy()
        # self.nums2[index:]=[]
        # self.nums2.append(val)
        # self.nums2+=a
        self.nums2[index]+=val



    def count(self, tot: int) -> int:
        count=0
        for i in range(tot):
            count+=self.nums1.count(i)*self.nums2.count(tot-i)

if __name__=="__main__":
    list1=[1, 1, 2, 2, 2, 3]
    list2=[1, 4, 5, 2, 5, 4]
    a=FindSumPairs(list1,list2)
    a.add(3,2)
    print(a.nums2)
