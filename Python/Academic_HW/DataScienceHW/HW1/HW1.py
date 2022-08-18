import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#   1A
v1 = np.arange(1, 101, 10)
print(v1)
#   1B
# v2 = np.arange(1, 101, 8)
# # 1C
# v2.reshape(2, 4)

# 2
df = pd.read_csv('customerData.csv')

# 2
df.describe()

# 2A
print("Number of Rows: {}, Number of Columns: {}".format(df.shape[0], df.shape[1]))

#   2B
for cat_name in df.columns:
    if pd.api.types.is_numeric_dtype(df[cat_name]):
        print("The Column {} is Numery".format(cat_name))
    elif pd.api.types.is_string_dtype(df[cat_name]):
        print("The Column {} is Category".format(cat_name))

# 2C - Cust id, is only for finding a specific customer purpose and because of that it isn't add us new data about
# the customer, and we can't use it for calculation


# 3
new_df = df.iloc[0::10, 0::2]
print(new_df)

# 4A
print(df.shape)

# 4B
print(df.size)

# 4C - Shape function - showing the dimension of the table(row and columns), Size function - showing number of
# elements in table

# 5
print(df[(38 <= df['age']) & (df['age'] <= 50)])

# 6A
print(df.select_dtypes(include=[np.number])[df['age'] > 50])

# 6B

# 7
new_seven_df = df['age'].head(100)
print(new_seven_df)

# 8
print(df[((df['marital_stat'] == "Married") | (df['marital_stat'] == "Divorced/Separated")) & (df['age'] < 18)]['custid'])

# 9
term_df = df[(df['income'] > 16000) & (df['state_of_res'] == 'Washington')]
# 9A
print("The mean age of people who live in washingtion and their income is bigger than 16000 is: {}"
      .format(term_df['age'].mean()))

#   9B
print("\nThe biggest age in term group is", term_df['age'].max())

# 9C
print("\nThe minimal salary in term group is:", term_df['income'].min())

# 9D
print("There are ", term_df.shape[0], " people that found by the terms")

#   10
new_df = df.groupby(['sex', 'housing_type'])['sex']
print(new_df.count().reset_index(name='Count', level='housing_type').sort_values(['Count'], ascending=False))

print("We can see that For Males the most popularity is Homeowner with mortgage/loan, and for female is Rented")
