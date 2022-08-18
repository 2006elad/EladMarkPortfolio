import math
import pstats

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.lines as mlines
import scipy.stats as stats

df = pd.read_csv('clubmed_HW2.csv')

#   1A
# plt.hist(df['age'], bins=20)
# plt.xlabel('Age')
# plt.ylabel('Quantity')
# plt.title("Age Histogram 20 bins")
# plt.show()
#
#
# #   1B
# plt.hist(df['age'],bins=10)
# plt.title("Age Histogram 10 bins")
# plt.show()
#
# plt.hist(df['age'], bins=50)
# plt.title("Age Histogram 50 bins")
# plt.show()

# The width of the bin is determined by the highest value less the lowest value, divided by the number of bin we set.
# The height (Y-axis), which is the quantity - is determined by the amount of observations that are in the same range of
# the same bin. That is - the smaller the bin number, the larger the range in each bin and the more observations it will
# have, and the wider bin will be. And vice versa, the more bin there are - the smaller the ranges will be, and then the
# quantity will be more accurate. That is - each bin will be narrower.


# 2
# bins = [-1, 30, 55, df['age'].max()+1]
# labels = ["young(18-30)", "mid(31-55)", "old(56-and more"]
# df['ageRange'] = pd.cut(df['age'], bins=bins, labels=labels)
# my_crosstab = pd.crosstab(df['ageRange'], df['club_member'])
# barplot = my_crosstab.plot.bar(rot=0)
# plt.show()

# 3
# df['fixed_total_expenditure'] = df['total_expenditure'].mask(df['total_expenditure'] < 0, np.nan)
# plt.hist(df['fixed_total_expenditure'])
# plt.show()
#
# df['log_total_expenditure'] = df['total_expenditure'].mask(df['total_expenditure'] < 0, np.nan)
# df['log_total_expenditure'] = np.log10(df['log_total_expenditure'])
# plt.hist(df['log_total_expenditure'])
# plt.show()

# When we log on a numeric column, the distribution becomes normal. With this you can study in a graph the
# distribution of the values, what the mean and median of the values are. And especially if we take the data
# for example a year later, it will be easy for us to check the differences between those two numeric columns.

#   4A
# group_by1 = df[['sex', 'status']].groupby(['sex', 'status']).size()
# my_crosstab1 = pd.crosstab(df['sex'], df['status'])
# print(group_by1)

#  4B
# my_crosstab2 = pd.crosstab(df['status'], df['sex'])
# print(my_crosstab2)

#   4C
# my_crosstab1.plot.bar(stacked=True)
# plt.show()
# my_crosstab2.plot.bar(stacked=True)
# plt.show()

# Answers for Questions:
# A. The biggest men's family status is: Couple.
# Inevitably the number of men in this status is the largest, as can be seen, the number of observations
# in "couple" status is more than half of the total number of men.

# B. The most frequent family status in females is: Couple.

# C. The married females percent is 70%

# D. The total males percent from singles is 50%

#   4D
# my_crosstab3 = pd.crosstab(df['ranking'], df['club_member'])
# my_crosstab3.plot.bar(stacked=True)
# plt.ylabel("Club_member")
# plt.title("Ratio between high rating and whether the customer is a club member")
# plt.show()
# It can be seen that: the higher the rating, the more likely it is that it is a club member

#   4E
# Q4e = pd.crosstab(index=df['sex'], columns=df['status'], normalize='index')
# Q4e.plot.bar(stacked=True, figsize=(8, 5), color=['pink','red','blue'])
# plt.legend(loc=(0.4, 0.1))
# plt.xticks(rotation=0)
# plt.title('Distribution of marital status by sex')
# plt.show()
#   It can be seen that the variable club_member has a greater trend relationship with the sex variable

#   5
# plt.scatter(df['age'], df['minibar'], color="purple")
# plt.xlabel("age")
# plt.ylabel("minibar")
# plt.title("The connection between age and minibar spend")
# plt.show()

#   6 A
# df[['room_price_new']] = df[['room_price']].fillna(value=df.room_price.mean())
# Q1 = df[['room_price_new']].quantile(0.25)
# Q2 = df[['room_price_new']].quantile(0.50)
# Q3 = df[['room_price_new']].quantile(0.75)
# IQR = Q3-Q1
# print("Q1", Q1)
# print("Q2", Q2)
# print("Q3", Q2)
# print('The IQR is: ', IQR)
# std = df[['room_price_new']].std()
# print('The std is: ', std)

#   6 B
# count = 0
# R_P_2_median = df.room_price_new.median()
# filtered_data = df[df.room_price_new <= R_P_2_median]
# print("the number of room price smaller than median", filtered_data["room_price_new"].count())
# No, because the median value is defined as a value out the group, with an equal number of values above and below it.

#   6C
# plt.hist(df[['room_price_new']])
# plt.axvline(df['room_price_new'].mean(), color='blue', linestyle='dashed', linewidth=1)
# plt.axvline(df['room_price_new'].mean() - df['room_price_new'].std(), color='red', linestyle='dashed', linewidth=1)
# plt.axvline(df['room_price_new'].mean() + df['room_price_new'].std(), color='red', linestyle='dashed', linewidth=1)
# plt.show()

#   6D
#   The distribution is not normal, it is tilted to the right

#   6E
df.boxplot(column=['age'], by='ranking', grid=False)
plt.show()
#   6.E.A Answer: Ranking two

#   6e.b
# df.boxplot(column=['age'], by='ranking', grid=False)
# plt.axhline(99)
# plt.axhline(21)
# plt.show()

#   6F
# df.boxplot(column=['age'], by='visits5years', grid=False)
# plt.show()

#   The number of visits for which the inter-quarter range is suitable for the oldest population is: 6,
# this group age range is: 34-56

#   6G
# bins = [-1, 20, 34, 56, df['age'].max()+1]
# labels = ["0-20", "21-33", "34-56", "57+"]
# df["ageAdjust"] = pd.cut(df['age'], bins=bins, labels=labels)
# df.boxplot(column=['room_price'], by='ageAdjust', grid=False)
# plt.show()

#   6H
df['total_expenditure'] = df['total_expenditure'].mask(df['total_expenditure'] < 0, np.nan)
df['total_expenditure'] = df['total_expenditure'].replace(to_replace=np.nan, value=df['total_expenditure'].mean())
fig, ax = plt.subplots()
ax.scatter(df['ranking'], df['total_expenditure'], c='black')
line = mlines.Line2D([0, 1], [0, 1], color='red')
transform = ax.transAxes
line.set_transform(transform)
ax.add_line(line)
plt.xlabel("ranking")
plt.ylabel("total_expenditure")
plt.title("The connection between ranking and total_expenditure")
plt.show()

#   7
# bins = [-1, 1, df["visits2016"].max()+1]
# labels = ["Signed in 2016, Didn't visit Yet ", "Visit already"]
# df['visits2016Adjust'] = pd.cut(df['visits2016'], bins=bins, labels=labels)
# df['visits2016Adjust'] = df['visits2016Adjust'].replace(to_replace=np.nan, value="Signed after 2016")
# print(df['visits2016Adjust'])

#   8A
# df['total_expenditure_new'] = df['total_expenditure'].mask(df['total_expenditure'] < 0, np.nan)
# df['total_expenditure_new'] = df['total_expenditure_new'].replace(to_replace=np.nan, value=df['total_expenditure'].mean())
# bins = [df['total_expenditure_new'].min()-1, df['total_expenditure_new'].describe()[4], df['total_expenditure_new'].describe()[5], df['total_expenditure_new'].describe()[6], df["total_expenditure_new"].max()+1]
# labels = ["Q1", "Q2", "Q3", "Q4"]
# df['total_expenditure_new'] = pd.cut(df['total_expenditure_new'], bins=bins, labels=labels)
# print(df['total_expenditure_new'])

#   8B - Replace with mean, because mean doesn't change the mean and statical details like std

#   8C

#   9A
# df["norm_minibar"] = stats.zscore(df["minibar"])
#
# #   9B
# print("The SD before normalize is: ", df["minibar"].std())
# print("The SD after normalize is: ", df["norm_minibar"].std())
#
# #   9C
# typical_values_count = 0
# for one_val in df["norm_minibar"]:
#     if -1.0 <= one_val <= 1.0:
#         typical_values_count += 1
# print("There are ", typical_values_count, "typical values")
