import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

credit_data = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Logistic Regression\\credit_risk.csv")
print(credit_data.info())

X = credit_data.columns.drop('class')
y = credit_data['class']

# Encoding categorical data
credit_data_encode = pd.get_dummies(credit_data[X])
print('Total predictors after encoding:',len(credit_data_encode.columns))
print(credit_data_encode.shape)

# Train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(credit_data_encode,y,test_size=0.15,random_state=100)

print("Shape of X_train and y_train are:", X_train.shape, "and", y_train.shape, " respectively")
print("Shape of X_test and y_test are:", X_test.shape, "and", y_test.shape, " respectively")

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=1)
model.fit(X_train,y_train)

train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

from sklearn.tree import export_graphviz 
import graphviz

dot_data = export_graphviz(model,out_file=None,feature_names=credit_data_encode.columns,class_names=model.classes_)
graph = graphviz.Source(dot_data)

train_accuracy = model.score(X_train,y_train) 
test_accuracy = model.score(X_test,y_test)    
print(train_accuracy,test_accuracy)

# As we can observe the train accuracy is coming out as 100% and on test it is 63% it means our model is overfitted on the data


# Min number of samples required in a set to split = 10
# Min reduction in impurity required for split to be included in the tree = 0.005
model1 = DecisionTreeClassifier(min_samples_split=10,min_impurity_decrease=0.005)
# Fitting the model to the training data
model1.fit(X_train,y_train)
# Measuring the accuracy of the model
print("train_accuracy = ", model1.score(X_train,y_train))
print("test_accuracy = ", model1.score(X_test,y_test))

# Model 2:
# Min number of samples required in a set to split = 20
# Min reduction in impurity required for split to be included in the tree = 0.1
model2 = DecisionTreeClassifier(min_samples_split=20,min_impurity_decrease=0.1)
# Fitting the model to the training data
model2.fit(X_train,y_train)
# Measuring the accuracy of the model
print("Model2 train accuracy = ", model2.score(X_train,y_train))
print("Model2 test accuracy = ", model2.score(X_test,y_test))


