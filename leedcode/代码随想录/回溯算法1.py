#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/3/5 9:01 
# @File : 回溯算法1.py 
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n + 1):  # 需要优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点

if __name__ == '__main__':
    n = 4
    k = 2
    A = Solution()
    a = A.combine(n, k)
    print(a)
