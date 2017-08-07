"""sorted(iterable, key=None, reverse=False)"""
fruits = ['Banana', 'Apple', 'Lime']

print(sorted(fruits))   # ['Apple', 'Banana', 'Lime']
print(sorted(fruits, reverse=True)) # ['Lime', 'Banana', 'Apple']

fruit_dict = {2:'Banana', 1:'Apple', 3:'Lime'}
print(fruit_dict.items())   # dict_items([(2, 'Banana'), (1, 'Apple'), (3, 'Lime')])
print(sorted(fruit_dict.items(), key=lambda fruit:fruit[1]))    # [(1, 'Apple'), (2, 'Banana'), (3, 'Lime')]
print(sorted(fruit_dict.items()))    # [(1, 'Apple'), (2, 'Banana'), (3, 'Lime')]

"""
all(iterable)
any(iterable)
"""
ss = ['abc', None, 'xyz']
print(all(ss))  # False
print(any(ss))  # True

"""zip(iter1, [, iter2[...]])"""
str_and_len = {str:length for str, length in zip(fruits, map(len, fruits))}
print(str_and_len)  # {'Banana': 6, 'Apple': 5, 'Lime': 4}
