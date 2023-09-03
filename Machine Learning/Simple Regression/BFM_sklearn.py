import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fitting the best fit model
computer = pd.read_csv(r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Demo\\review\\01_Simple Linear Regression\\Simple Linear Regression\\datasets\\computers.csv")

# Setting the predictors 
x = computer['Units']

# Setting the target feature
y = computer["Minutes"]

# Importing the required class
from sklearn.linear_model import LinearRegression

# Creating a linear regression model

model = LinearRegression()

# Fitting the model to the data 
model.fit(x,y)

# Fetching the intecept and coefficent
print(f"Intercept:{model.intecept_},Coefficients:{model.coef_}")

SST = sum((computer.Minutes.mean() - computer.Minutes)**2)

SSE = 348.848370927318 # Error of best fit model

SSR = SST - SSE

Rsq = SSR/SST

Rsq1 = model.score(computer['Units'],y)