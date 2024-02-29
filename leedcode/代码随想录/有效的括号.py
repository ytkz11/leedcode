#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/2/29 15:22 
# @File : 有效的括号.py 
from typing import List


class Solution:
    def function(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        for i in nums:
            if i =="{" or i =='(' or i =="[":
                a +=1
            if i == "}" or i == ')' or i == "]":
                a-=1
        if a!=0:

            return False
        else:
            return True





if __name__ == '__main__':
    nums = "{[]}"
    A = Solution()
    a = A.function(nums)
    print(a)
