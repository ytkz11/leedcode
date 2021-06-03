# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 9:12

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a = []

        for j in range(len(matrix[0])):
                for i in range(len(matrix) - 1, -1, -1):
                    a.append(matrix[i][j])

        matrix1 = []
        for idx in range(0, len(a), len(matrix[0])):
                matrix1.append(a[idx:idx+len(matrix[0])])

        return matrix1

if __name__ == '__main__':
    m =  [[1]]
    # m =[[1]]
    # m =[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    A = Solution()
    a1 = A.rotate(m)
    a = 0
