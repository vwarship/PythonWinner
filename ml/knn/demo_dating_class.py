import numpy as np
from ml.knn.knn import classify, auto_norm, draw_scatter_plots

"""约会配对
样本文件：datingTestSet.txt
每列的意思
    1 每年获得的飞行常客里程数
    2 玩视频游戏所耗时间百分比
    3 每周消费的冰淇淋公升数
    4 配对结果 [largeDoses smallDoses didntLike]
"""


filename = 'datingTestSet.txt'

label2int = {
    'largeDoses': 1,
    'smallDoses': 2,
    'didntLike': 3
}

k = 3


def file2matrix(filename):
    f = open(filename)
    lines = f.readlines()
    line_len = len(lines)

    dating_mat = np.zeros((line_len, 3))
    labels = []
    for n, line in zip(range(0, line_len), lines):
        line = line.strip()
        items = line.split('\t')
        dating_mat[n] = items[0:3]
        labels.append(label2int[items[-1]])

    f.close()

    return dating_mat, labels


def draw_dating_scatter_plots():
    dating_data, dating_lables = file2matrix(filename)
    draw_scatter_plots(dating_data[:, 1], dating_data[:, 2], dating_lables)


def test():
    dating_data, dating_lables = file2matrix(filename)
    dating_data_norm, dating_data_ranges, dating_data_min_vals = auto_norm(dating_data)
    dating_data_size = len(dating_data_norm)

    test_data_size = int(dating_data_size * 0.1)  # 取10%的大小

    test_data, test_lables= dating_data_norm[:test_data_size], dating_lables[:test_data_size]
    data, lables= dating_data_norm[test_data_size:], dating_lables[test_data_size:]

    error = 0
    for x, label in zip(test_data, test_lables):
        y = classify(x, data, lables, k)
        if y != label:
            error += 1
        print('分类为：{}, 实际为：{}. [{}]'.format(y, label, y!=label))

    print("error rate: {}%".format(error/float(test_data_size)*100.0))


def run():
    dating_data, dating_lables = file2matrix(filename)
    dating_data_norm, dating_data_ranges, dating_data_min_vals = auto_norm(dating_data)

    ffmiles = float(input("每年获得的飞行常客里程数："))
    percent_tags = float(input("玩视频游戏所耗时间百分比："))
    icecream = float(input("每周消费的冰淇淋公升数："))

    rating_data_with_person = [ffmiles, percent_tags, icecream]
    label = classify((rating_data_with_person-dating_data_min_vals)/dating_data_ranges,
             dating_data_norm, dating_lables, k)

    int2lable = {v:k for k, v in label2int.items()}
    print('你喜欢这个人：', int2lable[label])


# 画散点图
draw_dating_scatter_plots()

# 测试错误率
test()

# 实际应用
run()