#To establish a best fit linear regression model with minimum error the least squares method is used. For a linear regression model, every additional predictor variable tends to minimize the error of the model. As a result, the R2

# Model with a single predictor - n.prod
import pandas as pd
import numpy as np
delivery  = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Multi Regression\\delivery.csv")
features = ['n.prod']
target = ['delTime']

from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
model1.fit(delivery[features],delivery[target])
print(model1.score(delivery[features],delivery[target]))

# Model with mulitple predictor - n.prod , distance
model2 = LinearRegression()
features = ['n.prod','distance']
target = ['delTime']
model2.fit(delivery[features],delivery[target])
print(model2.score(delivery[features],delivery[target]))


# Computation of adjusted R square
X = delivery[features]
y = delivery[target]
adjusted_rscore = 1 - (1-model2.score(X,y))*(len(y)-1)/(len(y)-X.shape[1]-1)
print(adjusted_rscore)
print(X.shape[1])