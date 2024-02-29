#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/2/29 15:19 
# @File : 删除字符串中的所有相邻重复项.py 
from typing import List


# 方法一，使用栈
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and(res[-1] == item) :
                res.pop()
            else:
                res.append(item)
        return "".join(res)  # 字符串拼接

if __name__ == '__main__':
    nums = 'aaabaa'
    A = Solution()
    a = A.removeDuplicates(nums)
    print(a)
