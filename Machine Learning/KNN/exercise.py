# Consider the columns - duration, and age as predictors and the column “y”(indicates whether the client will subscribe for a term deposit) as the target variable

import pandas as pd
import numpy as np
df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Decision Tree\\bank-additional-full.csv")

X = df[['duration','age']]
y = df['y']

X_encoded = pd.get_dummies(X)
y_encoded = pd.get_dummies(y)
print(X_encoded)
print(y_encoded)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X_encoded)


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_normalized,y,test_size=0.4,random_state=0)

print('X Train:',X_train.shape)
print('Y Train:',y_train.shape)
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3,metric='euclidean')
model.fit(X_train,y_train)
train_score = model.score(X_train,y_train)
test_score = model.score(X_test,y_test)
print(train_score,test_score)

k_vals = [i for i in range(1,20)]
train_accuracies = []
test_accuracies = []

for i in k_vals:
    model = KNeighborsClassifier(n_neighbors=i,metric='euclidean')
    model.fit(X_train,y_train)
    train_accuracies.append(model.score(X_train,y_train))
    test_accuracies.append(model.score(X_test,y_test))

import matplotlib.pyplot as plt
plt.plot(k_vals,train_accuracies,marker='o',label="Train Accuracy")
plt.plot(k_vals,test_accuracies,marker='o',label="Test Accuracy")
plt.legend()
plt.show()