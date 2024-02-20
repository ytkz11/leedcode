#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/2/20 9:00 
# @File : remove_element.py 
import cv2
import numpy as np
import imageio
import matplotlib.pyplot as plt
from typing import List
class Solution2:
    def __init__(self):
        self.frames = []

    def function(self, nums: List[int], val: int) -> int:
        i, l = 0, len(nums)
        while i < l:
            if nums[i] == val:
                for j in range(i+1, l):
                    nums[j - 1] = nums[j]

                l -= 1
                i -= 1

            # 可视化当前状态
            self.visualize(nums, i, l)

            i += 1
        return l

    def visualize(self, nums, i, l):
        fig, ax = plt.subplots(dpi=80)
        nums_vis = nums.copy()
        nums_vis[l:] = [-1 for _ in range(len(nums) - l)]
        nums_2d = np.array(nums[:l]).reshape(1, -1)
        ax.imshow(nums_2d, cmap='nipy_spectral', aspect='auto')

        ax.axis('off')

        ax.text(i, 0.2, 'I', ha='center', va='center', color='r', fontsize=20)

        for index, num in enumerate(nums[:l]):
            ax.text(index, -0.2, str(num), ha='center', va='center', color='r', fontsize=20)
        ax.text(0, 0.6, f'length:{l+1}', ha='center', va='center', color='black', fontsize=20)

        fig.canvas.draw()
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.frames.append(img)

        plt.close()

    def save_gif(self, filename):
        with imageio.get_writer(filename, mode='I', fps=1) as writer:
            for frame in self.frames:
                writer.append_data(frame)
class Solution:
    def __init__(self):
        self.frames = []

    def function(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        size = len(nums)

        while fast < size:
            self.visualize(nums, slow, fast)
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

            # 可视化当前状态


            fast += 1
        return slow

    def visualize(self, nums, slow, fast):
        fig, ax = plt.subplots(dpi=80)

        nums_2d = np.array(nums).reshape(1, -1)
        ax.imshow(nums_2d, cmap='jet', aspect='auto')

        ax.axis('off')

        ax.text(slow, 0.2, 'S', ha='center', va='center', color='r',fontsize=20)
        ax.text(fast, 0.3, 'F', ha='center', va='center', color='g',fontsize=20)
        ax.text(0, 0.6, f'times:{slow+1}', ha='center', va='center', color='black', fontsize=20)
        for i, num in enumerate(nums):
            ax.text(i, -0.2, str(num), ha='center', va='center', color='r',fontsize=20)

        fig.canvas.draw()
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.frames.append(img)

        plt.close()

    def save_gif(self, filename):
        with imageio.get_writer(filename, mode='I', fps=1) as writer:
            for frame in self.frames:
                writer.append_data(frame)

if __name__ == '__main__':
    nums = [3,6,5, 2, 2, 3, 4, 2]
    val = 2
    A = Solution2()
    a = A.function(nums, val)
    A.save_gif('remove_element2.gif')
