import numpy as np
from ml.knn import *
from ml.knn.knn import *

"""
样本文件：datingTestSet.txt
每列的意思
    1 每年获得的飞行常客里程数
    2 玩视频游戏所耗时间百分比
    3 每周消费的冰淇淋公升数
    4 配对结果 [largeDoses smallDoses didntLike]
"""


def file2matrix(filename):
    f = open(filename)
    lines = f.readlines()
    line_len = len(lines)

    label2int = {
        'largeDoses': 1,
        'smallDoses': 2,
        'didntLike': 3
    }

    dating_mat = np.zeros((line_len, 3))
    labels = []
    for n, line in zip(range(0, line_len), lines):
        line = line.strip()
        items = line.split('\t')
        dating_mat[n] = items[0:3]
        labels.append(label2int[items[-1]])

    f.close()

    return dating_mat, labels


dating_data_filename = 'datingTestSet.txt'
dating_data, dating_lables = file2matrix(dating_data_filename)
draw_scatter_plots(dating_data[:, 1], dating_data[:, 2], dating_lables)

dating_data_norm, dating_data_ranges, dating_data_min_vals = auto_norm(dating_data)

print(dating_data_norm)