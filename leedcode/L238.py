# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 17:24
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        a = []
        for i in range(len(nums)):
            b1 = 1
            for j in nums[:i]+nums[i+1:]:
                b1 *= j

            a.append(b1)
        return a

if __name__ == '__main__':

    a1 = [1, 2, 3, 4]
    a1 = [0, 0]
    a = Solution()
    a = a.productExceptSelf(a1)

    a = 0