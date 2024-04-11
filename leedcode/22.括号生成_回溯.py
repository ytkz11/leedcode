#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/4/11 13:17 
# @File : 22.括号生成_回溯.py
from typing import List


def generateParenthesis(n):
    def generate(A = [], left = 0, right = 0):
        if len(A) == 2*n:
            ans.append("".join(A))
            return
        if left < n:
            A.append('(')
            generate(A, left+1, right)
            A.pop()
        if right < left:
            A.append(')')
            generate(A, left, right+1)
            A.pop()

    ans = []
    generate()
    return ans


if __name__ == '__main__':

    a = generateParenthesis(3)
    print(a)
