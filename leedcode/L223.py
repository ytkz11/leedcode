# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 10:36
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        if self.isinside(ax1, ax2, bx1) != 0:
            x1 = bx1
            if self.isinside(ay1,ay2,by1)!=False:

                y1 = by1
            else:

                y1 = by2
        else:
            x1 = bx2
            if self.isinside(ay1,ay2,by1)!=False:

                y1 = by1
            else:

                y1 = by2
        a = 0
        if self.isinside(bx1,bx2,ax1) !=False:

            if self.isinside(bx1,bx2,ay1)!=False:
                x2 = ax1
                y2 = ay1
            else:
                x2 = ax1
                y2 = ay2
        else:
            if self.isinside(bx1,bx2,ay1)!=False:
                x2 = ax2
                y2 = ay1
            else:
                x2 = ax2
                y2 = ay2
        return (x1-x2)*(y1-y2)


    def isinside(self, xx1, xx2,  x):
        if (x < xx2 and x > xx1) or (x > xx2 and x < xx1):

            x = x

        else:
            x = False
        return x

if __name__ == '__main__':
    ax1 = -3
    ay1 = 0
    ax2 = 3
    ay2 = 4
    bx1 = 0
    by1 = -1
    bx2 = 9
    by2 = 2
    A = Solution()
    a = A.computeArea( ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    a = 0