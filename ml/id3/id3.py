from math import log
import operator
import pickle


def calc_shannon_entropy(dataset):
    """计算香农熵
    熵超高，则混合的数据也越多.
    """

    total = len(dataset)
    label_counts = {}
    for data in dataset:
        label = data[-1]
        label_counts.setdefault(label, 0)
        label_counts[label] += 1

    shannon_entropy = 0.0
    for value in label_counts.values():
        prob = value / total
        shannon_entropy -= prob * log(prob, 2)

    return shannon_entropy


def split_dataset(dataset, feature_index, feature_value):
    """
    划分数据集
    :param dataset:待划分数据集
    :param feature_index: 划分数据集特征的索引
    :param feature_value: 需要返回特征的值
    :return: 返回划分后的数据集
    """

    new_dataset = []
    for data in dataset:
        if data[feature_index] == feature_value:
            new_data = data[:feature_index] + data[feature_index+1:]
            new_dataset.append(new_data)

    return new_dataset


def choose_best_feature_index(dataset):
    """
    选择数据集中的最佳特征
    :param dataset: 数据集
    :return: 最佳特征索引值
    """

    feature_num = len(dataset[0]) - 1   # 最后一列是实例特征属性
    base_entropy = calc_shannon_entropy(dataset)
    best_info_gain = 0.0
    best_feature_index = -1

    for i in range(feature_num):
        new_entropy = 0.0
        unique_feature_values = {data[i] for data in dataset}
        for feature_value in unique_feature_values:
            sub_dataset = split_dataset(dataset, i, feature_value)
            prob = len(sub_dataset) / len(dataset)
            new_entropy += prob * calc_shannon_entropy(sub_dataset)

        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature_index = i

    return best_feature_index


def majority(classes):
    class_count = {}
    for c in classes:
        class_count.setdefault(c, 0)
        class_count[c] += 1

    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_tree(dataset, labels):
    classes = [data[-1] for data in dataset]

    # 类别完全相同则停止划分
    if len(set(classes)) == 1:
        return classes[0]

    # 遍历完所有特征时返回出现次数最多的
    if len(dataset[0]) == 1:
        return majority(classes)

    best_feature_index = choose_best_feature_index(dataset)
    best_feature_label = labels[best_feature_index]

    sub_labels = labels[:]
    del(sub_labels[best_feature_index])

    tree = {best_feature_label: {}}

    unique_feature_values = {data[best_feature_index] for data in dataset}
    for feature_value in unique_feature_values:
        sub_dataset = split_dataset(dataset, best_feature_index, feature_value)
        tree[best_feature_label][feature_value] = create_tree(sub_dataset, sub_labels)

    return tree


def save_tree(tree, filename):
    with open(filename, 'wb') as f:
        pickle.dump(tree, f)


def read_tree(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
