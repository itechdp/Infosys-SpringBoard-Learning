import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fitting the best fit model
computer = pd.read_csv(r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Demo\\review\\01_Simple Linear Regression\\Simple Linear Regression\\datasets\\computers.csv")

x = computer.Units
y = computer.Minutes

xiyi = x*y
n = len(computer)
xmean = computer.Units.mean()
ymean = computer.Minutes.mean()
numerator = xiyi.sum() - n*xmean*ymean
denominator = (x**2).sum() - n*(xmean**2)
m = numerator/denominator
c = ymean - (m*xmean)
print(f'Intercept:{c} & Coefficient:{m}')

min_best_fit_model = c + m*computer.Units

# Adding the predicted values to the dataset
computer['min_best_fit_model'] = min_best_fit_model

# Printingthe values predicted by the best fit model
print(computer[['Units','Minutes',"min_best_fit_model"]])

# Visualizing the best fit model

fig,ax = plt.subplots()

# Plotting the actual target values
ax.scatter(x=computer.Units,y=computer.Minutes)

# Plotting the target values predicted by the best fit model
ax.plot(computer.Units,computer.min_best_fit_model,color='red')

ax.set_ylabel("Minutes")
ax.set_xlabel("Units")
ax.set_title("Best fit model line")

# Analyzing the error for the best fit model
# Computing the individual errors for the best fit model
best_fit_model_obs = pd.DataFrame({"Units":computer.Units,
              "Actual time":computer.Minutes,
              "Predicted time":computer.min_best_fit_model,
              "Error":computer.min_best_fit_model - computer.Minutes})

print(sum(best_fit_model_obs.Error**2))
