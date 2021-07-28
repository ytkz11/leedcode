class Solution:
    def subsets(self, nums) :
        self.res = []
        self.backtrack([], 0, nums)

        return self.res

    def backtrack(self, sol, index, nums):
        self.res.append(sol)

        for i in range(index, len(nums)):
            self.backtrack(sol + [nums[i]], i + 1, nums)



if __name__ == '__main__':
    nums = [1, 2, 3]
    A = Solution()
    a = A.subsets(nums)
    a = 0