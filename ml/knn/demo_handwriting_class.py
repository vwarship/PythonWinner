from os import listdir
from ml.knn.knn import classify
import numpy as np


"""手写数字识别"""

img_width = 32
img_height = 32

traing_digits_dir = 'digits/trainingDigits/'
test_digits_dir = 'digits/testDigits/'

k = 3


def img2vector(filename):
    vec = np.zeros((1, img_width*img_height))
    f = open(filename)
    for row_num in range(img_height):
        line = f.readline()
        for col_num in range(img_width):
            vec[0, row_num*img_width+col_num] = int(line[col_num])
    f.close()

    return vec


def dir2matrix(dir):
    filenames = listdir(dir)
    num = len(filenames)
    mat = np.zeros((num, img_width*img_height))
    labels = []
    for i, filename in zip(range(num), filenames):
        mat[i, :] = img2vector(dir + filename)
        labels.append(int(filename.split('_')[0]))

    return mat, labels


def test():
    training_digit_mat, training_digit_labels = dir2matrix(traing_digits_dir)
    test_digit_mat, test_digit_labels = dir2matrix(test_digits_dir)

    total = len(test_digit_mat)
    error = 0
    for test_mat, test_label in zip(test_digit_mat, test_digit_labels):
        label = classify(test_mat, training_digit_mat, training_digit_labels, k)
        print('识别的数字是：{}，实际数字是：{}。[{}]'.format(label, test_label, label==test_label))

        if label!=test_label:
            error += 1

    print("error rate: {}% error number: {}".format(error/float(total)*100.0, error))


"""测试结果
......
识别的数字是：1，实际数字是：8。[False]
识别的数字是：8，实际数字是：8。[True]
......
error rate: 1.0570824524312896% error number: 10
"""
test()
