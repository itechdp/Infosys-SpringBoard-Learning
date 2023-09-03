import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Analyzing the error
computer = pd.read_csv(r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Demo\\review\\01_Simple Linear Regression\\Simple Linear Regression\\datasets\\computers.csv")
print(computer.head())
print(computer.info())

# Regression Techniques: 
#  linear regression model involves only one predictor variable, it is called a Simple Linear Regression model. f(X) = ß0 + ß1x1 + ∈

#  linear regression model involves multiple predictor variables, it is called a Multiple Linear Regression model. f(X) = ß0 + ß1x1 + ß2x2 + ... + ßnxn + ∈

# Simple Linear Regression: Creating Regression Model

# Model 0: Time taken to repair a computer = 97.21 (i.e. mean)

# Model 1: Time taken to repair a computer = 10 + (12 * No. of Units being replaced)

# Model 2: Time taken to repair a computer = 6 + (18 * No. of Units being replaced)

min_model0 = computer['Minutes'].mean()
min_model1 = 10+12*computer['Units']
min_model2 = 6+18*computer['Units']
print((min_model0,min_model1,min_model2))

computer['min_model0'] = min_model0
computer['min_model1'] = min_model1
computer['min_model2'] = min_model2

# Model 0 assumed that time taken to repair the computer is constant and predicted using the mean

# Model 1, ß0 = 10, can be assumed as the startup time required to understand the repair work to be done The other coefficient, ß1 = 12 is assumed to represent the time required to replace a single unit of computer

# Similarly in Model 2, ß0 and ß1 are chosen to be 6 and 18 respectively.

# Visulizing the speculated regression model

fig,ax = plt.subplots()

# Plotting the actual minutes
ax.scatter(x='Units',y='Minutes',data=computer,label='actual repair time')

# Plotting the model0 predictions
ax.plot(computer['Units'],computer['min_model0'],color='red',label='Model 0')

# Plotting the model1 predictions
ax.plot(computer['Units'],computer['min_model1'],color='green',label='Model 1')

# Plotting the model2 predictions
ax.plot(computer['Units'],computer['min_model2'],color='black',label="Model 2")

# Adding xlabel, ylabel, title and legend 
ax.set_ylabel("Minutes")
ax.set_xlabel("Units")
ax.set_title("Speculated Models")
ax.legend()

#Analyzing the Speculated Models:
#The following code snippet shows the units replaced, the observed time taken, expected time taken (based on the model) and the difference between predicted and observed values for Model 0.

# Validating Model0: Estimated time = mean('Minutes')
# Creating a Pandas DataFrame with 'Units', actual 'Minutes', predicted 'Minutes' by Model0, error in prediction by Model0.
model0_obs = pd.DataFrame({"Units":computer['Units'],
              "Actual time":computer['Minutes'],
              "Predicted time":computer['min_model0'],
              "Error":(computer['min_model0'] - computer['Minutes'])})
print(model0_obs) # Printing the DataFrame

# analying model 0

# Sum of errors for model 0
print(sum(model0_obs['Error']))

# Applying sum of squared error to get the actual error rate for model 0

# SSE
print(sum(model0_obs['Error']**2))

# Analyzing model 1
# Creating a Pandas DataFrame with 'Units', actual 'Minutes', predicted 'Minutes' by Model1, error in prediction by Model1.
# Model1: Estimated time = 10 + 12*(#Units) minutes
model1_obs = pd.DataFrame({"Units":computer.Units,
              "Actual time":computer.Minutes,
              "Predicted time":computer.min_model1,
              "Error":(computer.min_model1 - computer.Minutes)})


# SSE for model 1
print(sum(model1_obs.Error**2))

# Analyzing model 2
# Creating a Pandas DataFrame with 'Units', actual 'Minutes', predicted 'Minutes' by Model2, error in prediction by Model2.
# Model2: Estimated time = 6 + 18*(#Units) minutes
model2_obs = pd.DataFrame({"Units":computer.Units,
              "Actual time":computer.Minutes,
              "Predicted time":computer.min_model2,
              "Error":(computer.min_model2 - computer.Minutes)})

# SSE for model 2
print(sum(model2_obs.Error**2))
