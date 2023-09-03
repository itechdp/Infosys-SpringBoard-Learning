import pandas as pd 
import numpy as np
path = r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\rainfall.csv"
dataset = pd.read_csv(path)
dataframe = pd.DataFrame(dataset)
print(dataframe)
print(dataframe.info())
print(dataframe.describe())

# Check for missing values, if any and drop the corresponding rows.
dataframe.dropna(inplace=True)

# Find the district that gets the highest annual rainfall.
annual_mean = dataframe['ANNUAL'].agg(np.mean,axis=0)
dist_high_fall = dataframe.loc[(dataframe['ANNUAL'] > 1346)]

# Display the top 5 states that get the highest annual rainfall.
top_5_dist_high_fall = dist_high_fall.head(n=5).sort_values(by='ANNUAL',ascending=True)

# Drop the columns 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec'.
print(dataframe.info())
dataframe.drop(['Jan-Feb','Mar-May','Jun-Sep','Oct-Dec'],inplace=True,axis=1)
print(dataframe.info())

# Display the state-wise mean rainfall for all the months using a pivot table.
pivot = pd.pivot_table(dataframe,index='STATE_UT_NAME',aggfunc=np.mean)
print(pivot)

# Display the count of districts in each state.
district_count = dataframe.groupby(['STATE_UT_NAME']).count()[['DISTRICT']]
print(district_count)

#For each state, display the district that gets the highest rainfall in May. Also display the recorded rainfall.
may_rainfall = dataframe.groupby(['MAY']).agg(np.max)[['DISTRICT']]
print(may_rainfall.sort_values(by='MAY',ascending=True))