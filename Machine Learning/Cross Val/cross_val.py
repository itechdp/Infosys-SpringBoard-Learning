# Implementing cross validation
import pandas as pd
import numpy as np
defaulter = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\KNN\\defaulter.csv")
print(defaulter.head())

# Normalizing the data using MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
features_to_scale = ['balance','income']
scaled_values = scaler.fit_transform(defaulter[features_to_scale])
print(scaled_values)
defaulter['norm_balance'] = scaled_values[:,0]
defaulter['norm_income'] = scaled_values[:,1]

# Splitting the data into train test 
from sklearn.model_selection import train_test_split
X = defaulter[['norm_balance','norm_income']]
y = defaulter['defaulter']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=100)

# Finding best value for KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
knn = KNeighborsClassifier()

# Create a dictionary of all k neighbor values
param_grid = {'n_neighbors':np.arange(1,15,2)}

# Using gridsearchcv to perform k fold validation
knn_gscv = GridSearchCV(knn,param_grid=param_grid,return_train_score=True,verbose=1,scoring='accuracy')
knn_gscv.fit(X_train,y_train)

df = pd.DataFrame(knn_gscv.cv_results_)
print(df.head())
df = df[['param_n_neighbors','mean_train_score','mean_test_score']]
print(df)

model = KNeighborsClassifier(n_neighbors=9,metric='euclidean')
model.fit(X_train,y_train)
train_accuracy = model.score(X_train,y_train)
test_accuracy = model.score(X_test,y_test)
print(train_accuracy,test_accuracy)