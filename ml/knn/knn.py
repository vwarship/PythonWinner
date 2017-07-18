import numpy as np
import operator


def classify(x, dataset, labels, k):
    """kNN(k近邻算法)
        1）计算测试数据与各个训练数据之间的距离；
        2）按照距离的递增关系进行排序；
        3）选取距离最小的K个点；
        4）确定前K个点所在类别的出现频率；
        5）返回前K个点中出现频率最高的类别作为测试数据的预测分类。
    使用欧氏距离公式 d=sqrt((x0-x1)^2+(y0-y1)^2)
    :param x: 要求的向量
    :param dataset: 数据集
    :param labels: 数据集对应的标记
    :param k: 取距离最小的前k个值
    :return:
    """

    dataset_size = dataset.shape[0]
    diff_mat = np.tile(x, (dataset_size, 1)) - dataset
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances**0.5

    sorted_distance_indexs = distances.argsort()
    label_count = {}
    for i in range(k):
        label = labels[sorted_distance_indexs[i]]
        label_count.setdefault(label, 0)
        label_count[label] += 1

    sorted_label_count = sorted(label_count.items(),
                                key=operator.itemgetter(1), # key=lambda e: e[1],
                                reverse=True)
    return sorted_label_count[0][0]


dataset = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
labels = ['A', 'A', 'B', 'B']
k = 3
x = [0,0]
y = classify(x, dataset, labels, k)
print(y)    # B
