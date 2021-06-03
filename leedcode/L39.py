# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 9:30
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    A = Solution()
    a = A.combinationSum(candidates,target)
    a = 0
