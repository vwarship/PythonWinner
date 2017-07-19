import numpy as np


d = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

"""min max"""
col_min_vals = d.min(0) # [1 2 3]
col_max_vals = d.max(0) # [7 8 9]

row_min_vals = d.min(1) # [1 4 7]
row_max_vals = d.max(1) # [3 6 9]


"""tile
[[1 2 3 1 2 3]
 [4 5 6 4 5 6]
 [7 8 9 7 8 9]
 [1 2 3 1 2 3]
 [4 5 6 4 5 6]
 [7 8 9 7 8 9]]
"""
np.tile(d, (2,2))
