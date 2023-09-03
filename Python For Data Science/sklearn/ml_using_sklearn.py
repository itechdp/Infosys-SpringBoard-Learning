import pandas as pd 
df = pd.read_csv('E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv')

# Data properties
df_info = df.info()

# Dropping null values
df.dropna(inplace=True)
df_info = df.info()

# Predictors and target

X = df.iloc[:,1:8] # Predictor
y = df.iloc[:,0] # Target

# Converting categorical values into dummy values
X = pd.get_dummies(X)

#The data must be divided into two parts. First, a training set on which model can be trained. Second, a testing set on which the model can be validated.

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

#'test_size = 0.2' represents that 20% of the data will be used as test set.

#Since all the variables in the data are with different units of measurements and different scales, it would be a good idea to standardize them. A standard scaler performs this operation by transforming the columns such that the mean of every column or variable is 0 and standard deviation is 1

# Applying standard scaler on the data

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
scale.fit_transform(X_train)
scale.transform(X_test)

#The linear regression model is used to build the model. A linear regression model uses the following equation:
#y = B0 + B1*X1 + B2*X2 + _ _ _ _ + Bn*Xn
#In this case, y refers to the target and X1,X2…..Xn refer to the predictors. B0 is the intercept  and B1,B2…..Bn are the coefficients.
#Below code demonstrates the Linear Regression model building using sklearn library on the training data set. 

# Importing and fitting the mkodel on traning set
from sklearn.linear_model import LinearRegression
reg = LinearRegression()

# Fitting the model on training data:
reg.fit(X_train,y_train)

# Checking coefficient(slope) and intercept
# 'm' reprecents the cofficient 'c' intecept
m,c = reg.coef_,reg.intercept_
print(m,c)

#Predicting the target: mpg against the predictors in the training data set
#Predicted data stored in y_pred_train
y_pred_train = reg.predict(X_test)

#Predicting the target: mpg against the predictors in the testing data set
#Predicted data stored in y_pred_test
y_pred_test = reg.predict(X_test)

#There are different metrics used to evaluate the performance of the model. Here the R Square score is used.

# Prediction accuracy in terms of how close is the predictred value of traget: mpg

from sklearn.metrics import r2_score
r2_s = r2_score(y_train,y_pred_train)
print(r2_s)
# # Prediction Accuracy in terms of how close the predicted value of target: mpg
# to the real value in testing data set

from sklearn.metrics import r2_score
r2_s = r2_score(y_test,y_pred_test)
print(r2_s)