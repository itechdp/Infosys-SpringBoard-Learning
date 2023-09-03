import pandas as pd

# Consider the column 'y' as the target variable. From the remaining columns, consider all except 'duration' as predictors.
dataset = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Decision Tree\\bank-additional-full.csv")
X = dataset.drop(['y','duration'],axis=1)
y = dataset['y']

# Encode the predictors to convert them to numerical data.
X_encoded = pd.get_dummies(X)
y_encoded = pd.get_dummies(y)
print(X_encoded.shape,y_encoded.shape)

# Split the data into train and test with a ratio of 80:20.
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_encoded,y_encoded,test_size=0.20,random_state=0)

# Build a model using Decision Tree algorithm, to predict the target.
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train,y_train)
test_predictions = model.predict(X_test)

train_score = model.score(X_train,y_train)
test_score = model.score(X_test,y_test)
print(f"Train Score:{train_score}\nTest Score:{test_score}")
from sklearn.metrics import classification_report
accuracy_report = classification_report(y_test,test_predictions)
print(f"Accuracy Report:{accuracy_report}")

model1 = DecisionTreeClassifier(min_samples_split=10,min_impurity_decrease=0.005)
model1.fit(X_train,y_train)
test_predictions1 = model1.predict(X_test)

train_score1 = model1.score(X_train,y_train)
test_score1 = model1.score(X_test,y_test)
print(f"Train Score:{train_score1}\nTest Score:{test_score1}")
from sklearn.metrics import classification_report
accuracy_report1 = classification_report(y_test,test_predictions1)
print(f"Accuracy Report:{accuracy_report1}")
