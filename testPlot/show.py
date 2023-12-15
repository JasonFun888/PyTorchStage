# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# 函数
x = np.linspace(-1, 1, 50)
y = 2 * x + 1

# 第一幅图
plt.figure(num=1, figsize=(3, 5))  # 显示框设置(一个该函数，就是一个单另的显示框)
plt.plot(x, y, color='orange', linewidth=3.0, linestyle='--')  # 画图设置
plt.show()  # 显示图片（类似于print())）

# 第二幅图
plt.figure(num=3, figsize=(5, 4))
plt.plot(2 * x + 1, 3 * y, color='green', linewidth=1.0, linestyle=':')
plt.plot(2 * x + 1, 3 * y ** 2, color='red', linewidth=1.0, linestyle='-')
plt.show()
