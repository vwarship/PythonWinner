list(enumerate('abc'))    #[(0, 'a'), (1, 'b'), (2, 'c')]

fruits = ['Banana', 'Apple', 'Lime']
list(enumerate(fruits)) # [(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]
list(enumerate(fruits, 1))  # [(1, 'Banana'), (2, 'Apple'), (3, 'Lime')]

"""
1 Banana
2 Apple
3 Lime
"""
for ranking, fruit in enumerate(fruits, 1):
    print(ranking, fruit)