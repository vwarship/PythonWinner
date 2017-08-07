import matplotlib.pyplot as plt

from tutorial.matplotlib import font_zh

# http://matplotlib.org/users/annotations_guide.html


def draw_annotate(text, xy_begin, xy_text):
    bbox_props = dict(boxstyle='Sawtooth,pad=0.6', fc='0.8')
    arrow_props = dict(arrowstyle='<-')
    ax = plt.subplot(111, frameon=False)
    ax.annotate(text, xy=xy_begin, xytext=xy_text,
                va='center', ha='center',
                bbox=bbox_props, arrowprops=arrow_props,
                fontproperties=font_zh)
    plt.show()

draw_annotate(U'注解', (0.1, 0.5), (0.5, 0.1))
