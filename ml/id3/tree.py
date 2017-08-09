import matplotlib.pyplot as plt

from tutorial.matplotlib import font_zh


decision_bbox_props = dict(boxstyle='Square', fc='0.8')
node_bbox_props = dict(boxstyle='Circle', fc='0.8')


def get_tree_depth(data):
    max_depth = 0
    for key, value in data.items():
        if isinstance(value, dict):
            cur_depth = 1 + get_tree_depth(value)
        else:
            return 1

        max_depth = max(max_depth, cur_depth)

    return max_depth


def get_tree_leaf_num(data):
    leaf_num = 0
    for key, value in data.items():
        if isinstance(value, dict):
            leaf_num += get_tree_leaf_num(value)
        else:
            leaf_num += 1

    return leaf_num


def draw_node(ax, text, bbox_props, parent_xy, xy):
    arrow_props = dict(arrowstyle='<-')
    ax.annotate(text, xy=parent_xy, xytext=xy,
                va='bottom', ha='center',
                bbox=bbox_props, arrowprops=arrow_props,
                fontproperties=font_zh)


def draw_mid_text(ax, parent_xy, xy, text):
    mid_x = (parent_xy[0] - xy[0]) / 2 + xy[0]
    mid_y = (parent_xy[1] - xy[1]) / 2 + xy[1]
    ax.text(mid_x, mid_y, text)


def draw_tree(ax, data, parent_xy, text, y_offset):
    leaf_num = get_tree_leaf_num(data)

    key = list(data.keys())[0]
    value = data[key]
    xy = (draw_tree.x_offset + (1.0 + leaf_num) / 2.0 / draw_tree.leaf_num_total, y_offset)
    draw_node(ax, key, decision_bbox_props, parent_xy, xy)
    draw_mid_text(ax, parent_xy, xy, text)
    y_offset -= 1.0 / draw_tree.depth_total

    for key, value in value.items():
        if isinstance(value, dict):
            draw_tree(ax, value, xy, key, y_offset)
        else:
            draw_tree.x_offset += 1.0 / draw_tree.leaf_num_total
            draw_mid_text(ax, parent_xy=xy, xy=(draw_tree.x_offset, y_offset), text=key)
            draw_node(ax, value, node_bbox_props, parent_xy=xy, xy=(draw_tree.x_offset, y_offset))


if __name__ == '__main__':
    tree_data = {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}, 2: 'no'}}

    draw_tree.depth_total = get_tree_depth(tree_data)
    draw_tree.leaf_num_total = get_tree_leaf_num(tree_data)

    # x需要递增，所以要声明为全局变量
    draw_tree.x_offset = -0.5/draw_tree.leaf_num_total
    y_offset = 1.0
    xy = (0.5, 1.0)

    ax = plt.subplot(111, frameon=False, xticks=[], yticks=[])
    draw_tree(ax, tree_data, xy, '', y_offset)
    plt.show()
