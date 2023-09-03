'''
Capstone Project: Explore Machine Learning using Python
When an employee quits the organization, they take way experience, skill, knowledge acquired over a period of time within the organization. This affects the organization and the impact is not only restricted to that but also brings the task of finding a suitable replacement. Mostly the suitable replacement is hired from external and it again adds time and cost to the organization.

The HR department of a multinational company would like to understand the reasons for premature exit of experienced employees using Machine Learning techniques. For achieving this, they must:

 

Explore the dataset and check if the data can be used as-is.
Determine the relationship between satisfaction level and working hours of employees who have left the organization.
Understand the effect of satisfaction level, department, promotion in last 5 years and salary level of employees who have left the organization.
Build  a machine learning model to predict the exit of employees.
 

Click here to download the dataset:

 

The dataset has roughly 15000 records with 10 columns, which are self-explanatory, namely: satisfaction_level, last_evaluation, number_project, average_monthly_hours, time_spend_company, Work_accident, left, promotion_last_5years, Department, salary.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Explore the dataset and check if the data can be used as-is.
dataset = pd.read_csv('E:\Programming languages\Python\Infosys SpringBoard\Machine Learning\Capstone Project\HR_comma_sep.csv')
print(dataset.info())

# Determine the relationship between satisfaction level and working hours of employees who have left the organization.
left_dataset = dataset[dataset['left']==0]
print(left_dataset.info())
correlations = np.corrcoef(left_dataset['satisfaction_level'],left_dataset['time_spend_company'])
print(correlations) # -0.16

vif_labels = left_dataset[['satisfaction_level','time_spend_company']]
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = pd.Series([variance_inflation_factor(vif_labels.values,idx) for idx in range(vif_labels.shape[1])],index=vif_labels.columns)
print(vif)

# Understand the effect of satisfaction level, department, promotion in last 5 years and salary level of employees who have left the
X = dataset[['satisfaction_level','Department','promotion_last_5years','salary']]
y = dataset['left']

# Encoding categorical data of X features
X_encoded = pd.get_dummies(X)

# Normalizing the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X_encoded)

# Splitting into train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_normalized,y,test_size=0.3,random_state=100)
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

# Model Building
from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier(n_estimators=100)
model.fit(X_train,y_train)
train_accuracy = model.score(X_train,y_train)
test_accuracy = model.score(X_test,y_test)
print(f"Train Accuracy:{train_accuracy}\nTest Accuracy:{test_accuracy}")
y_predictions = model.predict(X_test)
print(y_predictions[0])

from sklearn.metrics import classification_report
classification_report = classification_report(y_test,y_predictions)
print(classification_report)