import pandas as pd 
import numpy as np

# Consider 'variance', 'skewness', 'curtosis', 'entropy' columns as predictors and the column 'class' as the target  variable
dataset = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Logistic Regression\\data_banknote_authentication.csv")
print(dataset.head())
print(dataset.info())

X = dataset[['variance','skewness','curtosis','entropy']]
y = dataset['class']
print(X.head())
print(y.head())

# Build a logistic regression model. 
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X,y)
model_score = model.score(X,y)
model_predicted = model.predict(X)
print(model_score)
from sklearn.metrics import classification_report
accuracy_report = classification_report(y,model_predicted)
print(accuracy_report)