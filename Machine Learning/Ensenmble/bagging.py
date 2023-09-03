import pandas as pd
import numpy as np
spam_data = pd.read_csv('E:\Programming languages\Python\Infosys SpringBoard\Machine Learning\Ensenmble\spambase.csv')
print(spam_data.head())

# Splitting the data intro
from sklearn.model_selection import train_test_split
features = spam_data.columns.drop('spam')
target = 'spam'
X = spam_data[features]
y = spam_data[target]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=100)

# Model Building

from sklearn.ensemble import RandomForestClassifier
# building model with RandomforestClassifier with 10 underlying Decision tree models/ estimators
model = RandomForestClassifier(n_estimators=10,min_samples_split=20,min_impurity_decrease=0.05)
model.fit(X_train,y_train)
train_accuracy = model.score(X_train,y_train)
test_accuracy = model.score(X_test,y_test)
print(train_accuracy,train_accuracy)

features_imps = pd.DataFrame(np.array([features,model.feature_importances_]).T,columns=['features','imp'])
features_imps.sort_values(by='imp',ascending=False)
