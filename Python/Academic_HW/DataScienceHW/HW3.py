# #LIOR HAZOOM 205972078
# #ELAD MARK 316293638

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import utils
from sklearn import preprocessing
from sklearn import metrics

df = pd.read_csv("votersdata.csv")
#Q1
RSEED = 123
#Q2A
my_crosstab1 = pd.crosstab(index=df['vote'], columns=df['sex'], normalize='index')
my_crosstab1.plot.bar(stacked=True,figsize=(8,5), color=['blue','yellow'])
plt.legend(loc=(0.4,0.1))
plt.xticks(rotation=0)
plt.title("vote vs sex")
plt.show()
my_crosstab2 = pd.crosstab(index=df['vote'], columns=df['passtime'],normalize='index')
my_crosstab2.plot.bar(stacked=True,figsize=(8,5), color=['blue','purple','red'])
plt.legend(loc=(0.4,0.1))
plt.xticks(rotation=0)
plt.title("vote vs passtime")
plt.show()
my_crosstab3 = pd.crosstab(index=df['vote'], columns=df['status'],normalize='index')
my_crosstab3.plot.bar(stacked=True,figsize=(8,5), color=['red','blue','yellow'])
plt.legend(loc=(0.4,0.1))
plt.xticks(rotation=0)
plt.title("vote vs status")
plt.show()

#Q2B
df.boxplot(column=['age'], by='vote', grid=False)
plt.show()
df.boxplot(column=['salary'], by='vote', grid=False)
plt.show()
df.boxplot(column=['volunteering'], by='vote', grid=False)
plt.show()

#Q3
print(df.describe())

df["age"] = df["age"].mask(df["age"] < 18, np.nan)
df["age"] = df["age"].replace(to_replace=np.nan, value=df.age.mean())

print(df.isnull().sum())

df[['age_new']] = df[['age']].fillna(value=df.age.mean())
df[['salary_new']] = df[['salary']].fillna(value=df.salary.mean())
df['passtime'].describe()
df[['passtime_new']]=df[['passtime']].replace(to_replace=np.nan, value='fishing')

print(df.isnull().sum())

le = preprocessing.LabelEncoder()

le.fit(df["sex"].unique())
df['sex_encoded']= le.transform(df['sex'])

le.fit(df['passtime_new'].unique())
df['passtime_encoded']=le.transform(df['passtime_new'])

le.fit(df['status'].unique())
df['status_encoded']=le.transform(df['status'])

le.fit(df['vote'].unique())
df['vote_encoded'] = le.transform(df['vote'])
print(df.describe())

df_numerical = df[['sex_encoded','age_new','salary_new','volunteering','passtime_encoded','status_encoded','vote_encoded']]
df_normalized = stats.zscore(df_numerical)

#Q4
X = df_numerical.drop('vote_encoded', axis=1)
y = df_numerical[["vote_encoded"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RSEED)

#Q5
clf = DecisionTreeClassifier(random_state=RSEED)
clf = clf.fit(X_train, y_train)
fig = plt.figure(figsize=(14,10))
tree.plot_tree(clf, feature_names=X_train.columns, filled=True)
plt.show()
#tree.plot_tree(dt, feature_names= X_train.columns,class_names= y_train.columns,filled=True)
y_pred_test = clf.predict(X_test)
y_pred_traning=clf.predict(X_train)
#
#Q6
print(confusion_matrix(y_test,y_pred_test))
print("The results of the test: ")
print("Accuracy: ",metrics.accuracy_score(y_test, y_pred_test))
print("Precision: ",metrics.precision_score(y_test, y_pred_test))
print("Recall: ", metrics.recall_score(y_test, y_pred_test))
# #Q7
#
print(confusion_matrix(y_train,y_pred_traning))
print("the results of the train: ")
print("Accuracy: ",metrics.accuracy_score(y_train, y_pred_traning))
print("Precision: ",metrics.precision_score(y_train, y_pred_traning))
print("Recall: ", metrics.recall_score(y_train, y_pred_traning))
#Yes, the training results are all 1,
# while the test results are far from them when they are 0.85,0.87,0.88.
# Therefore there is overfitting.
#Q8
model = DecisionTreeClassifier(max_depth=5, min_samples_leaf=40)
model.fit(X_train, y_train)
tree.plot_tree(model, feature_names=X_train.columns , filled=True)
plt.show()
y_pred_test = model.predict(X_test)
y_pred_train = model.predict(X_train)
#Q8A
#The depth of the wood is 4
#Q8B
#the number of leafs is 6
#Q8C
#the best picher is
#Q8D
#yes: passtime_encoded, salary, vote_encoded
#Q8E
print("testing to see if the prediction is correct")
print(df.iloc[67])
# following the descision tree to see prediction
# the prediction is correct. The prediction and the target voting are the same = republican.
#Q9
print(confusion_matrix(y_test,y_pred_test))
print("The results of the test: ")
print("Accuracy: ",metrics.accuracy_score(y_test, y_pred_test))
print("Precision: ",metrics.precision_score(y_test, y_pred_test))
print("Recall: ", metrics.recall_score(y_test, y_pred_test))
print("train results: ")
print(confusion_matrix(y_train,y_pred_traning))
print("the results of the train: ")
print("Accuracy: ",metrics.accuracy_score(y_train, y_pred_traning))
print("Precision: ",metrics.precision_score(y_train, y_pred_traning))
print("Recall: ", metrics.recall_score(y_train, y_pred_traning))
#Q10**
# Q10
# We can conclude from the results that the model is accurate with no overfitting and underfitting.
# the results from the test and train sets are very close and look like each other.

#Q10
X_status = df_numerical.drop('status_encoded', axis=1)
y_status = df_numerical[["status_encoded"]]
X_train, X_test, y_train, y_test = train_test_split(X_status, y_status, test_size=0.3, random_state=RSEED)
new_tree = DecisionTreeClassifier(max_depth=5, min_samples_leaf=40,random_state=RSEED)
new_tree = new_tree.fit(X_train, y_train)
y_test_pred = new_tree.predict(X_test)
plt.show()
print(confusion_matrix(y_test,y_pred_test))
print("Accuracy: ",metrics.accuracy_score(y_test, y_pred_test))
#Accuracy:  0.5267857142857143
#Q10A
# The accuracy is low and this mean that the prediction for status is not so good and accurate.
# This accuracy shows that the true results where only in half of the occasions and that is no so good (underfiting).
#Q11
# couple = 0
# family = 1
# single = 2
# a copy of the confusion matrix
# [[9  17 0]
# [15 50 0]
# [ 18  3 0]]
#  single Precision = 18/(18+3+0) = 0.857