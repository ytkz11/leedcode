#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/2/27 17:28 
# @File : 反转字符串344.py 
from typing import List

'''
示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
'''
class Solution:
    def function(self, s) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = []
        for i in range(len(s),0,-1):
            new.append(s[i-1])
        a = 0

        return new


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    A = Solution()
    a = A.function(s)
    print(a)
