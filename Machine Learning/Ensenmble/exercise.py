import pandas as pd
dataset = pd.read_csv('Infosys SpringBoard\Machine Learning\Logistic Regression\data_banknote_authentication.csv')
print(dataset.info())

features = dataset.columns.drop('class')
target = 'class'

X = dataset[features]
y = dataset[target]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=100)

# Logistic regression model
from sklearn.linear_model import LogisticRegression
logistic_model = LogisticRegression()
logistic_model.fit(X_train,y_train)
logistic_train_acc = logistic_model.score(X_train,y_train)
logistic_test_acc = logistic_model.score(X_test,y_test)

# Desicion Tree
from sklearn.tree import DecisionTreeClassifier
decision_model = DecisionTreeClassifier()
decision_model.fit(X_train,y_train)
decision_train_acc = decision_model.score(X_train,y_train)
decision_test_acc = decision_model.score(X_test,y_test)

# AdaBoost
from sklearn.ensemble import AdaBoostClassifier
adaboost_model = AdaBoostClassifier(n_estimators=10)
adaboost_model.fit(X_train,y_train)
adaboost_train_acc = adaboost_model.score(X_train,y_train)
adaboost_test_acc = adaboost_model.score(X_test,y_test)

print(f"\nLogistic Regression Accuracy\nTrain Accuracy:{logistic_train_acc}\nTest Accuracy{logistic_test_acc}")

print(f"\nDecision Tree Accuracy\nTrain Accuracy:{decision_train_acc}\nTest Accuracy{decision_test_acc}")

print(f"\nAdaboost Accuracy\nTrain Accuracy:{adaboost_train_acc}\nTest Accuracy{adaboost_test_acc}")