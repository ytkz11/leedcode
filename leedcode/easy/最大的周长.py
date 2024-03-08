#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/3/8 16:10
# @File : 三角形的最大周长976.py
from typing import List


class Solution:
    def largestPerimeter(self,nums):
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
if __name__ == '__main__':
    nums = [1, 2, 10, 4]
    A = Solution()
    a = A.largestPerimeter(nums)
    print(a)
