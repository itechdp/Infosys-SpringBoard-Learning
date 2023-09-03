# King County House price dataset needs to be used for this exercise. Click here to download the King County House price dataset. The data represents the details of houses sold in King County, USA in 2014 and 2015. From the given features, predict the price of a house.

# Read data from input csv file
import pandas as pd
house_data = pd.read_csv(r'E:\\Programming languages\\Python\\Infosys SpringBoard\\Machine Learning\\Demo\review\\03_HousePricePrediction1603443197890\\House Price Prediction\\datasets\\kc_house_data.csv')
print(house_data.head())

# Determine the size of the data
print(house_data.shape) # (21613,21)

# Determine the columns in the data
print(house_data.columns)

# View information about the data in each columns 
print(house_data.info())

# Feature engineering

# Selecting the features
house_data_df = house_data[['price','date','bedrooms','bathrooms','sqft_living','floors','waterfront','view','condition','grade','zipcode']]

# Lets split date into year and month to consider that price could depend on year and month of sale due to market conditions Lets treat bedrooms, bathrooms, floors, waterfront, view, condition, grade, year and month as categorical features.

# Extracting year and month from date

house_data_df.loc[:,'year'] = house_data['date'].str[0:4]
house_data_df.loc[:,'month'] = house_data['date'].str[4:6]

# Removing date after extraction
house_data_df = house_data_df.drop(columns=['date'])

# Encoding categorical values 
cat_features = ['waterfront','view','condition','grade','year','month','zipcode']
house_data_df = pd.get_dummies(house_data_df,columns=cat_features)


# Normalizing the data
from sklearn.preprocessing import StandardScaler

# Finding the mean and std deviation of numerical columns
scaler = StandardScaler().fit(house_data_df[['price','bedrooms','bathrooms','sqft_living','floors']])

# Scaling columns to a common range
house_data_normalized = scaler.transform(house_data_df[['price', 'bedrooms', 'bathrooms', 'sqft_living', 'floors']])

# Output is 2D array of normalized data
print(house_data_normalized)

# Replacing the numerical columns with normalized values

house_data_df_nomralized = pd.DataFrame(house_data_normalized,columns=['price', 'bedrooms', 'bathrooms', 'sqft_living', 'floors'])

house_data_df_nomralized = house_data_df_nomralized.join(house_data_df[house_data_df.columns.drop(['price', 'bedrooms', 'bathrooms', 'sqft_living', 'floors'])])

# Selecting features and target 
y = house_data_df_nomralized['price']
X = house_data_df_nomralized[house_data_df_nomralized.columns.drop('price')]
print(X.shape)

# Splitting into train and test data

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=100)

# Model building and evaluate its performance suing R squared

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

# Evaluating the model on the train and test data fro R squared score
train_score = model.score(X_train,y_train)
test_score = model.score(X_test,y_test)
print("Train Score:",train_score)
print("Test Score:",test_score)

# Evaluating the model performance using RMSE
from sklearn.metrics import mean_squared_error

# Root mean error calculation for train data
train_predictions = model.predict(X_train)
train_RMSE = mean_squared_error(y_train,train_predictions)**0.5

# Root mean error calculation for test data
test_predictions = model.predict(X_test)
test_RMSE = mean_squared_error(y_test,test_predictions)**0.5

print("Train RMSE:",train_RMSE)
print("Test RMSE:",test_RMSE)


# Prediction accuracy of the regression model
#During the evaluation of a model on train and test data, following are the situations that may be faced:

# Model performance on train and test data is poor (High RMSE)

#Such models are typically referred to as underfit models because the model cannot explain the variation in the data reasonably. In such situations, quality and veracity of the data should be relooked and the features selected to build the model should be analysed. This might require more time and effort in engineering the features. 

# Model performance on train data is good (Low RMSE, High R-squared) but on test data is poor (High RMSE)

# Such models are typically referred to as overfit models, i.e. they have been fit perfectly for the train data but are not generalized enough. In such situations, we may need to:

# Gather more data instances as it is difficult to overfit larger size of data.

# Reduce the complexity of the model - Evaluate which features are important and use only those features to build the model.

 