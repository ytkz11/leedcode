#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/2/20 13:38 
# @File : sortedSquares.py 
from typing import List


class Solution:
    def sortedSquares(self, nums) -> None:
        """

        """
        s, e = 0, len(nums) - 1
        new_nums = nums.copy()
        for i in range(len(nums)-1,-1,-1):
            if nums[e]**2 > nums[s]**2:
                new_nums[i] = nums[e]**2
                e -= 1
            else:
                new_nums[i] = nums[s] ** 2
                s += 1
        return new_nums


if __name__ == '__main__':
    nums = [-5,-4,1, 2, 3]
    A = Solution()
    a = A.sortedSquares(nums)
    print(a)
