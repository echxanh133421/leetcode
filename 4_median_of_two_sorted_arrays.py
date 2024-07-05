class Solution:
    def findMedianSortedArrays(self, nums1, nums2) :

        n1 = len(nums1)
        n2 = len(nums2)

        list_final = []
        i = 0
        j = 0

        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                list_final.append(nums1[i])
                i += 1
            else:
                list_final.append(nums2[j])
                j += 1

        while i < n1:
            list_final.append(nums1[i])
            i += 1

        while j < n2:
            list_final.append(nums2[j])
            j+=1

        n=int(len(list_final))
        # return n
        if n%2==1:
            n=int(n/2)
            return list_final[n]
        else:
            n=int(n/2)
            return (list_final[n-1]+list_final[n])/2


if __name__=="__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    a=Solution()
    print(a.findMedianSortedArrays(nums1,nums2))