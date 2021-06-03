# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 14:18
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 14:17


class Solution:
    def myAtoi(self, s: str) -> int:
        s1 = ''
        for i in s:
            if i != " ":
                s1 += i
        del s
        a = ''
        for i in range(len(s1)):
            if s1[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']:
                if s1[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+', '.']:
                    a += s1[i]
            else:
                break
        if a != 0 and a != '':
            a1 = ''

            for i in range(len(a)):
                if a[i] != '.':
                    a1 += a[i]
                else:
                    break

            if a1[0] =='+':
                if len(a)<2:
                    a = 0
                else:
                    if a1[1] =='-':
                        a = 0


            if a1[0] == '-':
                if len(a)<2:
                    a = 0
                else:
                    if a1[1] == '+':
                        a = 0
            a = int(float(a))
            if a > 2 ** 31 - 1:
                a = 2 ** 31 - 1
            elif a < -2 ** 31:
                a = -2 ** 31
        else:
            a = 0

        return a

if __name__ == '__main__':

    a1 ="10"
    a = Solution()
    a = a.myAtoi(a1)
    a = 0