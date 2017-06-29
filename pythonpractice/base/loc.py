# coding=utf-8

import pandas as pd

data = [[1, 2, 3], [4, 5, 6]]
index = ['d', 'e']
column = ['a', 'b', 'c']

df = pd.DataFrame(data=data, index=index, columns=column)

print df

# iloc
print df.iloc[0][2]

print df.loc['d']



