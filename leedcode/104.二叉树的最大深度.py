#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/4/11 10:57 
# @File : 104.二叉树的最大深度.py.py 
from typing import List


class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    nums = [3,9,20,1,2,15,7]
    A = Solution()
    a = A.maxDepth(nums)
    print(a)
