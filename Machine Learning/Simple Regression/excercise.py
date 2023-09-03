# Use the Boston dataset (Click here to download the Boston dataset) and perform the following activities:
# 1.    Consider the column, ‘RM’, as predictor, and ‘MEDV’ as the target variable
# 2.    Visualize the association between the predictor and the target using scatter plot.
# 3.    Split the data into train and test datasets, in the ratio of 67:33.
# 4.    Build a Linear Regression model using training dataset, to predict the target variable.
# 5.    Observe the coefficient and intercept values for the model.
# 6.    Evaluate the model using mean squared error values and R-squared values on the training and the testing datasets.

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Regression\\boston_housing.csv")
print(dataset.info())

# Consider the column, ‘RM’, as predictor, and ‘MEDV’ as the target variable
x = dataset.RM
y = dataset.MEDV
print(x.head(),y.head())

# Visualize the association between the predictor and the target using scatter plot.
fig,ax = plt.subplots()
ax.scatter(x,y,marker='o')
ax.set_xlabel("RM")
ax.set_ylabel("MEDV")
ax.set_title("Association between Predictors & Target Value")

# Split the data into train and test datasets, in the ratio of 67:33.
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import numpy as np

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=42)

x_train = np.array(x_train).reshape(-1,1)
x_test = np.array(x_test).reshape(-1,1)
y_train = np.array(y_train).reshape(-1,1)
y_test = np.array(y_test).reshape(-1,1)

print(np.array(x_train).reshape(-1,1).shape,np.array(x_test).reshape(-1,1).shape)
#  Build a Linear Regression model using training dataset, to predict the target variable.
lin_reg = LinearRegression()
lin_reg.fit(x_train,y_train)
y_predicted = lin_reg.predict(x_test)

# Observe the coefficient and intercept values for the model.
print(lin_reg.coef_,lin_reg.intercept_)

# Evaluate the model using mean squared error values and R-squared values on the training and the testing datasets.
r2_score = r2_score(y_test,y_predicted)
print(r2_score)