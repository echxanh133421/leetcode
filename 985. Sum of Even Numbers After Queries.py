class Solution:
    def sum_even(self, nums):
        sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                sum += nums[i]
        return sum

    def sumEvenAfterQueries(self, nums, queries) :
        ls = []

        sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                sum += nums[i]

        for i in range(len(queries)):
            if nums[queries[i][1]] % 2 == 0:
                if queries[i][0] % 2 == 0:
                    sum+=queries[i][0]

                else:
                    sum-=nums[queries[i][1]]


            else:
                if queries[i][0] % 2 !=0:
                    sum+=queries[i][0] + nums[queries[i][1]]


            nums[queries[i][1]] += queries[i][0]
            ls.append(sum)
        return ls

if __name__=="__main__":
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]

    a=Solution()
    b=a.sumEvenAfterQueries(nums, queries)
    print(b)