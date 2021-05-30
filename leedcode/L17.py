
class Solution:
    def letterCombinations(self, digits: str):
        a ={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        b = []
        c= []
        for i in digits:


            b.append([x for x in a[i]])
        if len(b)<1:
            return []
        elif len(b)==1:
            return b[0]
        elif len(b)==2:
            for i in b[0]:
                for j in b[1]:
                    c .append(i+j)
            return c
        elif len(b)==3:
            for i in b[0]:
                for j in b[1]:
                    for k in b[2]:

                        c.append(i+j+k)
            return c
        elif len(b)==4:
            for i in b[0]:
                for j in b[1]:
                    for k in b[2]:
                        for l in b[3]:

                            c.append(i + j + k+l)
            return c




if __name__ == '__main__':
    A= Solution()
    a = A.letterCombinations('23')
    a = 0
    a = []
