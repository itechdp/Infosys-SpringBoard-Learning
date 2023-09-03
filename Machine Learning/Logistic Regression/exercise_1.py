# Exersicse
import pandas as pd
import numpy as np

# Consider duration, age, and campaign columns as predictors and the column “y”(states whether the client will subscribe a term deposit or not) as target  variable
dataset = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Logistic Regression\\bank-additional-full.csv")

print(dataset.info())
X = dataset[['age','duration','campaign']]
y = dataset['y']

# Use 70% of the data as training data set and 30% of data as testing data set.
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

# Build a logistic regression model.  
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
train_score = model.score(X_train,y_train)
test_score = model.score(X_test,y_test)

print(f'Train Score:{train_score} Test Score:{test_score}')