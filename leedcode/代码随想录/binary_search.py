import cv2
import numpy as np
from typing import List
import imageio
import matplotlib.pyplot as plt

class Solution:
    def __init__(self):
        self.frames = []

    def function(self, nums: List[int] , target: int) -> int:
        left, right = 0, len(nums) - 1
        iteration = 0
        while left <= right:
            mid = (left + right) // 2

            # 可视化当前状态
            self.visualize(nums, left, mid, right, iteration, final=(left==right))

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
            iteration += 1
        return -1

    def visualize(self, nums, left, mid, right, iteration, final=False):
        # 创建一个新的图形
        fig, ax = plt.subplots()

        # 使用imshow函数显示图像
        nums_2d = np.array(nums).reshape(1, -1)
        ax.imshow(nums_2d, cmap='nipy_spectral', aspect='auto')  # 更改颜色映射为 'nipy_spectral'

        # 隐藏坐标轴
        ax.axis('off')

        # 标记left、mid和right的位置
        ax.text(left, 0.2, 'L', ha='center', va='center', color='w')
        ax.text(mid, 0.3, 'M', ha='center', va='center', color='w')
        ax.text(right, 0.2, 'R', ha='center', va='center', color='w')

        # 在每个元素位置上添加一个文本标签，向上移动一些
        for i, num in enumerate(nums):
            ax.text(i, -0.2, str(num), ha='center', va='center', color='r')

        # 显示当前的迭代次数
        ax.text(0, -0.01, f'Iteration: {iteration+1}', ha='left', va='center', color='b')

        # 如果是最后一次迭代，添加 'final' 标签
        if final:
            ax.text(len(nums)-1, -0.01, 'Final', ha='right', va='center', color='g')

        # Convert the figure to cv2 image and add it to frames
        fig.canvas.draw()
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        self.frames.append(img)

        plt.close()

    def save_gif(self, filename):
        # Save frames as gif
        with imageio.get_writer(filename, mode='I',fps=1) as writer:
            for frame in self.frames:
                writer.append_data(frame)

if __name__ == '__main__':
    nums = [-1, 0, 1,2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    A = Solution()
    a = A.function(nums, 19)
    A.save_gif('binary_search.gif')
