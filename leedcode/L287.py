# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 9:30
class Solution:
    def findDuplicate(self, nums) -> int:


            slow = fast = cir_start = 0
            while True:
                fast = nums[nums[fast]]
                slow = nums[slow]
                if fast == slow:
                    break

            while True:
                slow = nums[slow]
                cir_start = nums[cir_start]
                if cir_start == slow:
                    return slow



if __name__ == '__main__':

    a1 = [1,2, 3, 4,3,6,5]

    a = Solution()
    a = a.findDuplicate(a1)

    a = 0