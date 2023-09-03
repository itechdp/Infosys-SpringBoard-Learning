import pandas as pd
iris_data = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\SVM\\iris.csv")
print(iris_data.head())

#Feature engineerng

#creating new column 'v_nv', to distinguish versicolor species from rest
#the below lambda function returns 0 for 'versicolor' species and returns 1 for rest.
v_nv_fn = lambda x: 0 if x=='versicolor' else 1

# new column added into dataframe
iris_data['v_nv'] = iris_data['Species'].apply(v_nv_fn)
print(iris_data[iris_data['v_nv']==0].head())

# Visualization sing seaborn pair plot
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(iris_data,x_vars='Petal.Length',y_vars='Petal.Width',hue='v_nv',height=5)

# Model Creation
from sklearn.svm import SVC
X = iris_data[['Petal.Length','Petal.Width']]
y = iris_data['v_nv']

model = SVC()
model.fit(X,y)
model.score(X,y)

from mlxtend.plotting import plot_decision_regions
import numpy as np
features = np.array(X)
target = np.array(y).ravel()
plot_decision_regions(features,target,clf=model)
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Decision boundry of SVM on iris data")
plt.tight_layout()

# Multiclass classification

#Encoding the species column
iris_data.loc[iris_data.Species=='setosa','Species'] = 0
iris_data.loc[iris_data.Species=='versicolor','Species'] = 1
iris_data.loc[iris_data.Species=='virginica','Species'] = 2
iris_data.Species = iris_data.Species.astype("category") 
# Multiclass model building
X = iris_data[['Petal.Length','Petal.Width']]
y = iris_data['Species']
model = SVC()
model.fit(X,y)

from mlxtend.plotting import plot_decision_regions
features = np.array(X)
target = np.array(y)
plot_decision_regions(features,target,clf=model)
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.title('Multiclass classification on iris using SVM')
plt.show()
