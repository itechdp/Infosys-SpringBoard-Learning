import pandas as pd
import numpy as np

dataset = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Multi Regression\\boston_housing.csv")
print(dataset.info())

# Consider the columns, ‘RM’, ‘DIS’, ‘TAX’, ‘INDUS’ as predictors, and ‘MEDV’ as the target variable
dataset_features = dataset[['RM','DIS','TAX','INDUS']]
print(dataset_features.head())

dataset_target = dataset['MEDV']
print(dataset_target.head())

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(dataset_features[['RM','DIS','TAX','INDUS']])
dataset_features_normalized = scaler.transform(dataset_features[['RM','DIS','TAX','INDUS']])
scaler = StandardScaler().fit(np.array(dataset_target).reshape(-1,1))
dataset_target_normalized = scaler.transform(np.array(dataset_target).reshape(-1,1))
print(dataset_features_normalized)

# Calculate the Variance Inflation Factor for each of the selected predictors. Based on the VIF factor, finalize the list of predictors.
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = pd.Series([variance_inflation_factor(pd.DataFrame(dataset_features_normalized).values,idx) for idx in range(dataset_features.shape[1])],index=dataset_features.columns)
print(vif)

#   For every predictor identified, visualize its association with the target column using scatter plot.
import matplotlib.pyplot as plt
ax1 = plt.scatter(dataset_features[['RM']],dataset_target)
ax2 = plt.scatter(dataset_features[['DIS']],dataset_target)
ax3 = plt.scatter(dataset_features[['TAX']],dataset_target)
ax4 = plt.scatter(dataset_features[['INDUS']],dataset_target)

ax1.set_label("RM")
ax2.set_label('DIS')
ax3.set_label('INDUS')
ax4.set_label('TAX')

plt.xlabel("Home Features")
plt.ylabel("Price")
plt.legend()

X = pd.DataFrame(dataset_features_normalized)
y = pd.DataFrame(dataset_target_normalized)
print(X.head(),y.head())

# Split the data into train and test datasets, in the ratio of 67:33.
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=100)

# Build a Linear Regression model, to predict the target variable using the selected predictors.
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(X_train,y_train)

# Observe the coefficients and intercept values for the model. 
print(linear_reg.coef_,linear_reg.intercept_)
train_score = linear_reg.score(X_train,y_train)
test_score = linear_reg.score(X_test,y_test)
print(f"Train Score:{train_score}\nTest Score:{test_score}")

from sklearn.metrics import mean_squared_error
# RMSE Score
y_test_predicted = linear_reg.predict(X_test)
test_rmse = mean_squared_error(y_test,y_test_predicted)**0.5

y_train_predicted = linear_reg.predict(X_train)
train_rmse = mean_squared_error(y_train,y_train_predicted)**0.5

# Evaluate the model using mean squared error values, R-squared values, and adjusted R-Squared values, on the train and the test data.
print(f"Train RMSE:{train_rmse}\nTest RMSE:{test_rmse}")
adjusted_r_train = 1 - (1-train_score)*(len(y_train)-1)/(len(y)-X_train.shape[1]-1)
adjusted_r_test = 1 - (1-test_score)*(len(y_train)-1)/(len(y)-X_test.shape[1]-1)
print('Adjsuted R Square Train:',adjusted_r_train)
print('Adjsuted R Square Test:',adjusted_r_test)