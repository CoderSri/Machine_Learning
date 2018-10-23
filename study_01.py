import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.optimize import leastsq
import scipy.optimize as opt
import scipy
import matplotlib.pyplot as plt
import math

def print_array(a):
    print('{} \nshape:{}, type:{} \n'.format(a, a.shape, type(a)))


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    print("L = ", L, '\ntype:', type(L), '\n')

    a = np.array(L)
    print_array(a)

    b = a.reshape(-1, 1)
    print_array(b)

    c = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    print_array(c)

    d = c.reshape(9, 4)
    print_array(d)

    e = np.array([[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]])
    print_array(e)

    f = e.reshape(4, -1)
    print_array(f)

    e[2][2] = 100
    print_array(f)  # 事实上e和f共享内存

    g = np.array([[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]], dtype=float)  # 指定数据类型
    print_array(g)

    h = g.astype(np.int)  # 重新制定数据类型
    print_array(h)

    i = np.linspace(1, 10, 20)  # 包含10  linspace 做等差数列
    print_array(i)

    j = np.linspace(1, 10, 20, endpoint=False)  # 不包含10
    print_array(j)

    k = np.logspace(1, 2, 20, endpoint=False)  # 不包含10 logspace 做等比数列 此处 2为 10的2次方=100
    print_array(k)

    l = np.logspace(0, 10, 11, endpoint=True, base=2)  # logspace 做等比数列 此处base为基底
    print_array(l)  # 2^0, 2^1, ... ,2^10

    s = 'abcd'
    g = np.fromstring(s, dtype=np.int8)
    print_array(g)

    a = np.arange(10)
    print_array(a)
    print_array(a[3:6])
    print_array(a[1:6:2])
    print_array(a[::-1])

    a = np.random.rand(10)
    print(a)
    print(a > 0.5)

    b = a[a > 0.5]  # 取a中大于0.5的数
    print(b)

    a = np.arange(0, 60, 10).reshape((-1, 1))
    print(a)
    b = np.arange(6)
    print(b)
    c = a + b
    print(c)

    # 二维数组的切片
    print(c[(0, 1, 2, 3), (2, 3, 4, 5)])
    print(c[3:, [0, 2, 5]])

    # 设置title字体
    # matplotlib.rcParams['font.sans-serif'] = [u'SimHei']  # FangSong/黑体 FangSong/KaiTi
    # matplotlib.rcParams['axes.unicode_minus'] = False

    # 画图 高斯分布
    mu = 0
    sigma = 1

    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50)
    y = np.exp(-(x - mu)**2/(2*sigma**2))/(math.sqrt(2*math.pi) * sigma)
    print_array(x)
    print_array(y)
    # plt.plot(x, y, 'ro-', linewidth=2)
    plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)
    plt.grid(True)
    plt.title('高斯分布')
    plt.show()

    