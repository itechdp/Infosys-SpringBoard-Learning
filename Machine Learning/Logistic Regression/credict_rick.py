import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

credit_data = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Logistic Regression\\credit_risk.csv")

# Understandign the values the 'class' column (target column in this analysis)
print(credit_data['class'].unique())

# Encode the categorical data

# Selecting predictors as all columns expect the class column
X = credit_data.columns.drop('class')
y = credit_data['class']

# Encoding all the featues/ predictors valriable usign the get dummines method()
credit_data_encoded = pd.get_dummies(credit_data[X])
print(credit_data_encoded.shape)

# Train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(credit_data_encoded,y,test_size=0.15,random_state=100)

# Checking the shapes of the resulting datasets
print("Shape of X_train:", X_train.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_test:", y_test.shape)

# Building the model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
train_acc = model.score(X_train,y_train)
test_ac = model.score(X_test,y_test)

print("Train Accuracy:",train_acc)
print("Test Accuracy:",test_ac)

# Checking for the confusion matrix
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# confusion matrix class
from sklearn.metrics import confusion_matrix
# For training data
train_conf_matrix = confusion_matrix(y_train,train_predictions)

# Converting confusion matrix to dataframe 
print(pd.DataFrame(train_conf_matrix,columns=model.classes_,index=model.classes_))

# For testing data
test_conf_matrix = confusion_matrix(y_test,test_predictions)
print(pd.DataFrame(test_conf_matrix,columns=model.classes_,index=model.classes_))

# Calculating the accuracy for our training and test dataset 

# Calculating train accuracy from confusion matrix
train_correct_predictions = train_conf_matrix[0][0] + train_conf_matrix[1][1]
train_total_predictions = train_conf_matrix.sum()
train_accuracy = train_correct_predictions/train_total_predictions
print("Train Confusion matrix accuracy:",train_accuracy)


# Calculating test accuracy from confusion matrix
test_correct_predictions = test_conf_matrix[0][0] + test_conf_matrix[1][1]
test_total_predictions = test_conf_matrix.sum()
test_accuracy = test_correct_predictions/test_total_predictions
print("Train Confusion matrix accuracy:",test_accuracy)

# Getting Precision,Recall,F1 Scoring report
from sklearn.metrics import classification_report
print(classification_report(y_test,test_predictions))
