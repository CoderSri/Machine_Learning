import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import preprocessing
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def iris_type(s):
    it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return it[s]


if __name__ == '__main__':
    path = u'8.iris.data'  # 数据文件路径
    # # 手写读取数据
    f = open(path)
    x = []
    y = []
    # for d in f:
    #     d = d.strip()
    #     if d:
    #         d = d.split(',')
    #         y.append(d[-1])
    #         x.append(list(map(float, d[:-1])))
    # x = np.array(x)
    # y = np.array(y)
    # y[y == 'Iris-setosa'] = 0
    # y[y == 'Iris-versicolor'] = 1
    # y[y == 'Iris-virginica'] = 2
    # y = y.astype(dtype=np.int)
    # # print(x)
    # # print(y)

    # # 使用sklearn的数据预处理
    #     # df = pd.read_csv(path, header=0)
    #     # x = df.values[:, :-1]
    #     # y = df.values[:, -1]
    #     # le = preprocessing.LabelEncoder()
    #     # le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    #     # print(le.classes_)
    #     # y = le.transform(y)
    #     # print(y)

    # 路径， 浮点型数据， 逗号分隔， 第4列使用函数iris_type单独处理
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    x, y = np.split(data, (4,), axis=1)
    # 为了可视化，使用前两列特征
    x = x[:, :2]
    # x = StandardScaler().fit_transform(x)
    # lr = LogisticRegression()  # Logistic回归模型
    # print(y.ravel())
    # lr.fit(x, y.ravel())
    # 等价形式
    lr = Pipeline([('sc', StandardScaler()), ('clf', LogisticRegression())])
    lr.fit(x, y.ravel())

    # 画图
    N, M = 500, 500
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, M)
    x1, x2 = np.meshgrid(t1, t2)  # 生成网络采样点(不明白，看文档)  x1，x2的shape:500x500
    x_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点   shape:250000 x2
    # print(x1.flat.shape)  # flat是将数组转化为一维的迭代器
    # print(x_test)

    cm_light = mpl.colors.ListedColormap(['#77E0A0', '#FF8080', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
    y_hat = lr.predict(x_test)          # 预测值 shape:250000x1
    # print(y_hat.shape)
    y_hat = y_hat.reshape(x1.shape)  # 使之与输入的形状相同 shape:500x500
    plt.pcolormesh(x1, x2, y_hat, cmap=cm_light)    # 预测值得显示

    plt.scatter(x[:, 0], x[:, 1], c=y.ravel(), edgecolors='k', s=50, cmap=cm_dark)   # 样本的显示
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.grid()
    plt.savefig('2.png')
    plt.show()


    # 训练集上的预测结果
    y_hat = lr.predict(x)
    y = y.reshape(-1)
    result = y_hat == y
    print(y_hat)
    print(result)
    acc = np.mean(result)
    print('准确度： %.2f%' % (100 * acc))
