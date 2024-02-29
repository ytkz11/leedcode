#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/2/20 14:16 
# @File : minSubArrayLen.py 
from typing import List

#  不太理解
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0


if __name__ == '__main__':
    nums = [1, 2, 3, 5, 8, 2, 4, 6, 2, 3]
    A = Solution()
    a = A.minSubArrayLen(10, nums)
    print(a)
