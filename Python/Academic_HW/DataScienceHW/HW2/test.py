

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier, plot_tree


df = pd.read_csv("500_persons.csv")
print(df.head())


print(df.info())
print(df.dtypes)

df.fitness.unique()
# We use the LabelEncoder to encode the categorical variables

le = LabelEncoder()
le.fit(df['fitness'])
df['new_fitness'] = le.transform(df['fitness'])

#df.new_fitness.unique()
#le.inverse_transform(df.new_fitness.unique())

print(df[['fitness', 'new_fitness']].head())


le_gender = LabelEncoder()
le_gender.fit(df['Gender'])
df['new_Gender'] = le_gender.transform(df['Gender'])
df[['Gender', 'new_Gender']].head()

#df.new_Gender.unique()
#le_gender.inverse_transform(df.new_Gender.unique())

df2 = df.drop(['fitness', 'Gender'], axis=1)
df2.head()


# split to x and y
X = df2.drop('new_Gender', axis=1)
y = df2['new_Gender']


#


# Set a constant number so the computer’s random generator will always select the same value.
# This number will be used in the next slides.
RSEED = 49


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=RSEED)


# ## Tree Without test set

print(df2.head())
# build a model and fit it on the entire dataset
model = DecisionTreeClassifier(random_state=RSEED)
model.fit(X_train, y_train)
# plot a huge, overfitted tree


plt.figure(figsize=(15, 17), dpi=300)
plot_tree(model, filled=True, feature_names=X.columns, class_names=le_gender.inverse_transform(model.classes_)
          , fontsize=6)
plt.show()

print(df2.head())
# limiting parameters
model = DecisionTreeClassifier(max_depth=5, min_samples_leaf=20)
model.fit(X_train, y_train)

y_pred_test = model.predict(X_test)
y_pred_train = model.predict(X_train)


print(df2.head())
plt.figure(figsize=(8, 8), dpi=300)
plot_tree(model, filled=True, feature_names=X.columns,
          class_names=le_gender.inverse_transform(model.classes_), fontsize=8)
plt.show()

print(df2.head())
plt.figure(figsize=(15, 17), dpi=300)
plot_tree(model, filled=True, feature_names=X.columns,
          class_names=le_gender.inverse_transform(model.classes_), fontsize=6)
plt.show()

plt.figure(figsize=(8, 5), dpi=100)
plot_tree(model, filled=True, feature_names=X.columns,
          class_names=le_gender.inverse_transform(model.classes_), fontsize=8)
plt.show()
