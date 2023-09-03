import pandas as pd
defaulter = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\KNN\\defaulter.csv")
print(defaulter.head())

import seaborn as sns
sns.pairplot(defaulter,hue='defaulter',x_vars='income',y_vars='balance',height=4)

# Euclidian distance between features
x1 = defaulter.loc[0,['balance','income']]
print(x1)

x2 = defaulter.loc[1,['balance','income']]
print(x2)

# Finding the distance between first and second data point
import numpy as np
distance = np.linalg.norm(x1-x2)
print(distance)

# Limitations of euclidian is that attributes with larger ranges contribute more value to the Euclidean distance.

t1 = np.array([26,1000])
t2 = np.array([66,1000])
t3 = np.array([36,10000])
dist_t3_t1 = np.linalg.norm(t3-t1)
dist_t2_t3 = np.linalg.norm(t2-t3)
print("Distance between t2 and t3",dist_t2_t3,
      "\nDistance between t1 and t3",dist_t3_t1)

# Normalization is essential to take into consideration, the different measurement scales of the attributes. Normalization is not just applied to kNN, it is often considered as a good practice to normalize the data before running any machine learning algorithm. 

# Normalizing the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler_valued = scaler.fit_transform(defaulter[['balance','income']])
defaulter['norm_balance'] = scaler_valued[:,0]
defaulter['norm_income'] = scaler_valued[:,1]
print(defaulter['norm_balance'])
print(defaulter['norm_income'])
print(defaulter.head())

# Disatnce between two normalized datapoints
x1_n = defaulter.loc[0,['norm_balance','norm_income']]
x2_n = defaulter.loc[1,['norm_balance','norm_income']]
distance_n = np.linalg.norm(x1_n-x2_n)
print(distance_n)

# Prediction based on 'k' Nearset neighbors
x11 = defaulter.loc[10,['norm_balance','norm_income']]
dist_to_x11 = lambda x: np.linalg.norm(x-x11)
defaulter['dist_toX11'] = defaulter[['norm_balance','norm_income']].apply(dist_to_x11,axis=1)
print(defaulter.sort_values('dist_toX11'))

# Model Building
from sklearn.model_selection import train_test_split
X = defaulter[['norm_balance','norm_income']]
y = defaulter['defaulter']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=100)
print(X_train.shape,y_train.shape)
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3,metric='euclidean')
model.fit(X_train,y_train)
train_accuracy = model.score(X_train,y_train)
test_accuracy = model.score(X_test,y_test)
print(train_accuracy,test_accuracy)

train_accuracies = []
test_accuracies = []

# Setting k value 1 to 100
k_vals = [i for i in range(1,7)]

features = ["norm_balance","norm_income"]
target = "defaulter"

for k in k_vals:
    model = KNeighborsClassifier(n_neighbors=k,metric='euclidean')
    model.fit(X_train,y_train)
    train_accuracy_k = model.score(X_train,y_train)
    test_accuracy_k = model.score(X_test,y_test)
    train_accuracies.append(train_accuracy_k)
    test_accuracies.append(test_accuracy_k)

import matplotlib.pyplot as plt
plt.plot(k_vals,train_accuracies)
plt.plot(k_vals,test_accuracies)
plt.show()