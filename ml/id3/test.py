from ml.id3.id3 import calc_shannon_entropy
from ml.id3.id3 import split_dataset
from ml.id3.id3 import choose_best_feature_index


dataset = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]

print(calc_shannon_entropy(dataset))    # 0.9709505944546686
print(split_dataset(dataset, 0, 0))     # [[1, 'no'], [1, 'no']]
print(split_dataset(dataset, 0, 1))     # [[1, 'yes'], [1, 'yes'], [0, 'no']]
print(choose_best_feature_index(dataset))   # 0
