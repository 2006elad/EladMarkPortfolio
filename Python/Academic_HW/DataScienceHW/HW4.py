# #LIOR HAZOOM 205972078
# #ELAD MARK 316293638

#QUESTION 1
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn import metrics
import scipy.stats as stats
import math
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('EnergyEfficiencyHW4.csv')
random_state=8123
# print(df.head())
print(df.columns)
# print(df.dtypes)

#Q1.1

X = df.drop('Heating Load', axis=1)
y = df["Heating Load"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

#Q1.2
regressor=linear_model.LinearRegression()
regressor.fit(X_train,y_train)
y_test_pred=regressor.predict(X_test)
print("test: ", mean_squared_error(y_test,y_test_pred,squared=False))

y_train_pred=regressor.predict(X_train)
print("train: ", mean_squared_error(y_train,y_train_pred,squared=False))

#Q1.3
rmse_test=mean_squared_error(y_test,y_test_pred,squared=False)
rmse_train=mean_squared_error(y_train,y_train_pred,squared=False)

#Q1.4
print(regressor.intercept_)

#Q1.5A
print(np.column_stack((X_train.columns, regressor.coef_)))
#We found that that: 'Orientation' recieved the smallest coefficient - 0.0223

#Q1.5B
# It is hard to understand, which variable is affecting the prediction more
# Because the data isn't normalized, coeffiencts are relative to their respective series
# As a result the data isn't on the same scale

#Q1.6

y_train_z=(y_train-y_train.mean())/y_train.std()
y_train_mn=y_train.mean()
y_train_std=y_train.std()

#X-Train
cols=['Glazing Area Dist', 'Glazing Area','Orientation','Overall Hight', 'Roof Area', 'Wall Area', 'Surface Area',
        'Relative Compactness']
X_train_z=pd.DataFrame(columns=cols)

for col in cols:
    col_zscore=col
    X_train_z[col_zscore]=(X_train[col]-X_train[col].mean())/X_train[col].std()

mean_dict = {}
std_dict = {}
for col in cols:
    mean_dict["%s" %col] = X_train[col].mean()
for col in cols:
    std_dict["%s" %col] = X_train[col].std()

regressor.fit(X_train_z,y_train_z)

#Y-test
y_test_z=(y_test-y_train_mn)/y_train_std

#X-test
X_test_z=pd.DataFrame(columns=cols)

for col in cols:
    col_zscore=col
    X_test_z[col_zscore]=(X_test[col]-mean_dict[col])/std_dict[col]

y_test_pred=regressor.predict(X_test_z)
y_train_pred=regressor.predict(X_train_z)

print("\nTest:", rmse_test,"\n Train:", rmse_train)
print('\n')

#Q1.7
print("Q7\n",np.column_stack((X_train_z.columns,regressor.coef_)))
# We can see that now the data is scaled. So, we can say that 'Overall Hight' is the most influence on Heating Load


#Q1.8
from sklearn.preprocessing import LabelEncoder
dtree_reg=DecisionTreeRegressor(max_depth=2,random_state=random_state)
dtree_reg.fit(X_train_z, y_train_z)
plt.figure(figsize=(10,10))
tree.plot_tree(dtree_reg,filled=True,feature_names=X.columns, class_names=['area'])
plt.show()

y_pred_test = dtree_reg.predict(X_test_z)
print("MSE & RMSE on test set")
print("Mean Squared Error:", mean_squared_error(y_test_z, y_pred_test))
print("Root Mean Squared Error:", mean_squared_error(y_test_z, y_pred_test,squared=False))
y_pred_train = dtree_reg.predict(X_train_z)
print("MSE & RMSE on train set")
print("Mean Squared Error:", mean_squared_error(y_train_z, y_pred_train))
print("Root Mean SquaredError:",mean_squared_error(y_train_z,y_pred_train,squared=False))

#QUESTION 2
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn import metrics
import math
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('memmographic_massesHW4.csv')
#Q2.1
df.dropna()
df.drop(df[df['Age']>120], axis=1)
# print(df.head())
# print(df.shape)
print(df.isnull().sum())
print(df.describe(include='all'))
#there is no Problematic or missing values
#Q2.2
random_state=8123
X = df.drop('Severity', axis=1)
y = df[["Severity"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
#Q2.3
clf=LogisticRegression(random_state=random_state)
clf.fit(X_train,y_train)
#Q2.4
y_train_pred=clf.predict(X_train)
print("the accuracy on the set train is: ",accuracy_score(y_train,y_train_pred))
print("the precision on the set train is: ",precision_score(y_train,y_train_pred))
print("the recall on the set train is: ",recall_score(y_train,y_train_pred))
y_test_pred=clf.predict(X_test)
print("the accuracy on the set train is: ",accuracy_score(y_test,y_test_pred))
print("the precision on the set train is: ",precision_score(y_test,y_test_pred))
print("the recall on the set train is: ",recall_score(y_test,y_test_pred))

#  QUESTION 3
#Q3.1
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn import metrics
import math
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import scipy.stats as stats
df = pd.read_csv('wine.csv')
#Q3.2
random_state=8123
y = df["Alcohol"]
X = df.drop('Alcohol', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
#Q3.3
train_size=X_train.shape[0]
k=round(math.sqrt(train_size)/2)
if k % 2 == 0:
    k += 1
print("the value is: ",k)
classifier=KNeighborsClassifier(n_neighbors=k)
classifier.fit(X_train,y_train)

y_test_pred=classifier.predict(X_test)
y_train_pred=classifier.predict(X_train)

train_ct=pd.crosstab(y_train,y_train_pred,colnames=['pred'], margins=True)
print("~~~~ Train  ~~~~ \n",train_ct)

print("Accuracy is: ", accuracy_score(y_train,y_train_pred))

train_percision=train_ct.iloc[0,0]/train_ct.iloc[3,0]
print("Percision is ", train_percision)

train_recall=train_ct.iloc[0,0]/train_ct.iloc[0,3]
print("Recall is: ", train_recall)


test_ct=pd.crosstab(y_test,y_test_pred,colnames=['pred'],margins=True)
print("\n~~~~   Test   ~~~~ \n",test_ct)

print("Accuracy is: ", accuracy_score(y_test,y_test_pred))

test_percision=test_ct.iloc[0,0]/test_ct.iloc[3,0]
print("Percision is:", test_percision)

test_recall=test_ct.iloc[0,0]/test_ct.iloc[0,3]
print("Recall is:", test_recall)



#Q3.4

print("Current k:", k)

accuracy=[]

for i in range (3,14):
    knn=KNeighborsClassifier(n_neighbors= i)
    knn.fit(X_train,y_train)
    pred_i=knn.predict(X_test)
    accuracy.append(accuracy_score(y_test,pred_i))

plt.figure(figsize=(12, 6))
plt.title("K Accuracy plot")
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.plot(range(3,14),accuracy,color='blue',linestyle='dashed', marker='o',markerfacecolor='brown', markersize=17)
plt.show()

print("We found that most accurated k is 4")
accurated_k=4

#Q3.5

df_z=df.drop(['Alcohol'],axis=1)
df_z=df.apply(stats.zscore)
print(df_z)

y=df.Alcohol
X=df_z


X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=8123)

classifier=KNeighborsClassifier(n_neighbors=accurated_k)
classifier.fit(X_train,y_train)

y_train_pred=classifier.predict(X_train)
y_test_pred=classifier.predict(X_test)

train_ct=pd.crosstab(y_train,y_train_pred,colnames=['pred'], margins=True)
print("~~~~ Train ~~~~ \n",train_ct)

print("Accuracy is: ", accuracy_score(y_train,y_train_pred))

train_precision=train_ct.iloc[0,0]/train_ct.iloc[3,0]
print("Precision is:", train_precision)

train_recall=train_ct.iloc[0,0]/train_ct.iloc[0,3]
print("Recall is:", train_recall)


test_ct=pd.crosstab(y_test,y_test_pred,colnames=['pred'],margins=True)
print("\n~~~~  Test  ~~~~ \n",test_ct)

print("Accuracy is : ", accuracy_score(y_test,y_test_pred))

test_precision=test_ct.iloc[0,0]/test_ct.iloc[3,0]
print("Precision is:", test_precision)

test_recall=test_ct.iloc[0,0]/test_ct.iloc[0,3]
print("Recall is :", test_recall)

# QUESTION 4
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn import metrics
import math
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import scipy.cluster.hierarchy as sch
df = pd.read_csv('wine.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.columns)

#Q4.1
print("The unique values of 'Alcohol' column are:", df.Alcohol.unique())
k=3

#Q4.2
features=df.drop(['Alcohol'],axis=1)
features_z=features.apply(stats.zscore)
print(features_z)

#Q4.3
random_state=8123
kmean=KMeans(n_clusters=k,random_state=random_state)
kmean.fit(features_z)

#Q4.4
print("\n",kmean.cluster_centers_,"\n")

#Q4.5
features['cluster']=kmean.labels_

#Q4.6
features_z['cluster']=kmean.labels_
print("the normals: ",features_z.groupby(features_z.cluster).mean(),"\n")
print("the regulars: ",features.groupby(features.cluster).mean(),"\n")
# ON Cluster 0:
#     Most:
#          ~ Malic Acid
#          ~ Alcalinity of ash
#          ~ Total Phenols
#          ~ Flavanoids
#          ~ Nonflavanoid phenols
#          ~ Color intensity
#          ~ OD280/OD315 of diluted wines
#          ~ Proline

#       Least:
#          ~ Magnesium
#          ~ Proanthocyanins
#

# On Cluster 1:
#   Most:
#      ~ Ash
#      ~ Magnesium
#      ~ Proanthocyanins
#      ~ Hue
#
#   Least:
#       ~ Flavanoids
#       ~ Nonflavanoid phenols
#       ~ Color intensity
#       ~ OD280/OD315 of diluted wines
#       ~ Proline

# On Cluster 2:
#   Most:
#           None
#
#   Least:
#       ~ Malic Acid
#       ~ Ash
#       ~ Alcalinity of ash
#       ~ Total Phenols
# We found that Cluster 1 has the highest of magnesium values

#Q4.7
#  K mean is Unsupervised learning, and it is  different from supervised learning. we don't have any output to compare
#  with the true labels, to calculate the perfomance. we only investagte the structure of data(by grouping into
#  subgroup with k-mean group technique)

#Q4.8
model=sch.linkage(features_z, method='complete')
plt.figure(figsize=(25,20))
dendrogram=sch.dendrogram(model)
plt.show()
#   We can see that there are 5 clusters.
