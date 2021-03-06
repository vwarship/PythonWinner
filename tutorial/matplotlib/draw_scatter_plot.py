import matplotlib.pyplot as plt
import numpy as np


def draw_scatter_plot():
    """绘制散点图"""
    data_mat = np.array(
        [[7.29170000e+04, 7.10627300e+00, 2.23600000e-01],
         [1.42830000e+04, 2.44186700e+00, 1.90838000e-01],
         [7.34750000e+04, 8.31018900e+00, 8.52795000e-01],
         [1.24290000e+04, 4.43233100e+00, 9.24649000e-01],
         [2.52880000e+04, 1.31899030e+01, 1.05013800e+00],
         [4.91800000e+03, 3.01112400e+00, 1.90663000e-01]])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data_mat[:, 1], data_mat[:, 2])
    plt.show()

draw_scatter_plot()
