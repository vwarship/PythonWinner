from ml.id3.id3 import create_tree
from ml.id3.tree import draw_tree_figure


with open('lenses.txt') as f:
    lenses = [line.strip().split('\t') for line in f.readlines()]

lenses_labels = ['age', 'prescript', 'astigmatic', 'tearrate']

lenses_tree = create_tree(lenses, lenses_labels)
print(lenses_tree)
draw_tree_figure(lenses_tree)