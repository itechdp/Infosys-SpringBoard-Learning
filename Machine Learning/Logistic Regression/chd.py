import pandas as pd
import numpy as np
chd = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Logistic Regression\\chd_data.csv")
print(chd.head())

# The variable chd = 0 indicates the absence of coronary heart disease, whereas chd=1 indicates the presence of coronary heart disease.

# Plotting the 'chd' values against 'age' values
import matplotlib.pyplot as plt
plt.scatter('age','chd',data=chd)
plt.xlabel("Age")
plt.ylabel("Chd")
plt.title("Age VS. Coronary Heart Diserase")

# Building a logistic regression model
from sklearn.model_selection import train_test_split

# Specifying the columns as predictor and target variable
predictor = ['age']
target = 'chd'

X = chd[predictor]
y = chd[target]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

# Checking the shapes of the resulting datasets
print("Shape of X_train",X_train.shape)
print("Shape of X_test",X_test.shape)
print("Shape of y_train",y_train.shape)
print("Shape of y_test",y_test.shape)

# Building model Logistic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
print("Intercept:",model.intercept_,"\nCoefficients:",model.coef_)

# Creating a sample data
test = np.array([29]).reshape(-1,1)

# Predicting the probablilites for each of the calss labels
print("Predicted Probablility for class '0' and '1' respectively:",model.predict_proba(test))

# Predicting the final class label or target value
print("Predicted target 'chd' values:",model.predict(test))

# Getting accuracy
print('Train Model Score:',model.score(X_train,y_train))
print("Test Model Score",model.score(X_test,y_test))
