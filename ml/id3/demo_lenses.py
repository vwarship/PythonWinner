from ml.id3.id3 import create_tree
from ml.id3.id3 import classify
from ml.id3.draw_tree import draw_tree_figure


"""预测患者需要佩戴的隐形眼镜类型"""


def get_dataset(language = None):
    filename = 'lenses.txt'
    lenses_labels = ['age', 'prescript', 'astigmatic', 'tearrate']

    if language == 'cn':
        filename = 'lenses_cn.txt'
        lenses_labels = ['年龄', '视力诊断', '散光', '眼泪流速']

    with open(filename) as f:
        lenses = [line.strip().split('\t') for line in f.readlines()]

    return lenses, lenses_labels

dataset, labels = get_dataset('cn')
lenses_tree = create_tree(dataset, labels)

# 测试
test_datas = [['中年', '近视', '否', '减少'],
              ['中年', '近视', '否', '正常']]
for data in test_datas:
    print('测试向量：{}，结果：{}'.format(data, classify(lenses_tree, labels, data)))

draw_tree_figure(lenses_tree)