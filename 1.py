import pandas as pd

data = {'A': [1, 2, None, 4],
        'B': [None, 5, 6, 7]}
df = pd.DataFrame(data)

# Using isnull()
print(df.isnull())

# Using isna() (which is equivalent to isnull())
print(df.isna())