# Read the data from input csv file
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
delivery  = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Multi Regression\\delivery.csv")
print(delivery.head())
print(delivery.info())

# Building a multiple linear regression model

from sklearn.linear_model import LinearRegression

model = LinearRegression()

# Selecting the predictors and targets
X = delivery[['n.prod','distance']]
y = delivery['delTime']

# Building the model using fit() method
model.fit(X,y)
print("Intercept:",model.intercept_,' Coefficients:',model.coef_)

# Visualizing Multiple Linear Regression model
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111,projection="3d")

# 3D scatter plot of the devlier dataset
ax.scatter(xs=delivery['n.prod'],ys= delivery['distance'],
           zs=delivery['delTime'],
           c='blue',
           alpha=1,
           marker='o')

ax.set_xlabel("n.prod")
ax.set_ylabel('Distance')
ax.set_zlabel("delTime")

# Creating a mesh of x and y vales to plot the regression plane
x_surf = np.arange(delivery['n.prod'].min(),delivery['n.prod'].max(),1)
y_surf = np.arange(delivery['distance'].min(),delivery['distance'].max(),1)
x_surf,y_surf = np.meshgrid(x_surf,y_surf)
X_mesh = pd.core.frame.DataFrame({'n.prod':x_surf.ravel(),'distance':y_surf.ravel()})

# Predicting the output of model for eery point in the mesh
out = model.predict(X_mesh)

# Plotting the regression planes
ax.plot_surface(x_surf,y_surf,out.reshape(x_surf.shape),alpha=0.4)
plt.show()

# MultiCollinearity
#In a multiple regression model where two or more predictor variables are involved, it is possible that one predictor can be linearly predicted from the others, with a substantial degree of accuracy.

# Due to collinearity, the coefficient estimates (ß0, ß1, ß2.) ​of the multiple regression may change erratically in response to small changes in the model or the data. But, for a linear regression model to be valid, it is essential that the predictors of the model are linearly independent of each other.

#Variance Inflation Factor
#In addition to correlation, there is another measure called variance inflation factor(VIF) to determine if the predictor variables are independent of each other.

# Linear independence of predictor for delivery time dataset
# finding the correlation

correlation = np.corrcoef(delivery['n.prod'],delivery['distance'])
print(correlation)

# Computing the VIF

from statsmodels.stats.outliers_influence import variance_inflation_factor

# Calculating the vif for each attributes
vif = pd.Series([variance_inflation_factor(X.values,idx) for idx in range(X.shape[1])],index=X.columns)
print(vif)

# Detemination of r2 score of the model
score = model.score(X,y)
print(score)

# You must be able to recall that the values of R2 ranges between 0 and 1 in Simple Linear Regression. The higher the value of R2 (close to 1), the model is considered as useful.

 