class Solution:
    def reverse(self, x: int) -> int:

        x1 = str(x)
        x2 = ''
        x4 = 1

        for i in reversed(x1):
            if i == '0':
                x3 = ''
            elif i == '-':
                x4 = -1
                x3 = ''
            else:
                x3 = i

            x2 += x3
        x2 = int(x2) * x4

        if x2 == '' or x2 < (-2) ** 31 or x2 > (2) ** 31 - 1:
            x2 = 0
        return x2
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A= Solution()
    a = A.reverse(202)
    a = 0
    a = []
