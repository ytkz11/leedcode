#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/4/11 9:48 
# @File : L3.py 
from typing import List


class Solution:
    def function(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict,res,i = {}, 0, -1
        for j in range(len(nums)):
            if nums[j] in dict:
                i = max(dict[nums[j]],i)

            dict[nums[j]] = j
            res = max(res, j - i)
        return res

if __name__ == '__main__':
    nums = 'abcabcbb'
    A = Solution()
    a = A.function(nums)
    print(a)
