from ml.id3.id3 import calc_shannon_entropy
from ml.id3.id3 import split_dataset
from ml.id3.id3 import choose_best_feature_index
from ml.id3.id3 import create_tree
from ml.id3.tree import draw_tree_figure


dataset = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]
labels = ['no surfacing', 'flippers']

print(calc_shannon_entropy(dataset))    # 0.9709505944546686
print(split_dataset(dataset, 0, 0))     # [[1, 'no'], [1, 'no']]
print(split_dataset(dataset, 0, 1))     # [[1, 'yes'], [1, 'yes'], [0, 'no']]
print(choose_best_feature_index(dataset))   # 0
print(create_tree(dataset, labels))     # {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}

print(dataset, labels)
tree_data = create_tree(dataset, labels)
draw_tree_figure(tree_data)