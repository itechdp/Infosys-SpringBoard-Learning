import numpy as np 
import pandas as pd

series = pd.Series(data=[78,92,35,64,89])
print(series)
print(series.values,series.index)
print(series[1])
print(series[1:3])
data = pd.Series(data=[700000,800000,1600000,1800000,200000],index = ['Swift','Jazz','Civic','Altis','Gallardo'])
print(data)
print(data['Swift'])
print(data['Jazz': 'Gallardo'])

#Using dictionary to create a series
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
print(car_price)

#Creating a car price series with a dictionary
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
# Creating the car manufacturer series with a dictionary
car_man_dict = {'Swift' : 'Maruti',
                  'Jazz'   : 'Honda',
                  'Civic'  : 'Honda',
                  'Altis'  : 'Toyota',
                   'Gallardo' : 'Lamborghini'}
car_man = pd.Series(car_man_dict)
print(car_price)
print(car_man)

cars = pd.DataFrame({'price':car_price,'Manufacturer':car_man})
print(cars)
print(cars['price'])
print(cars['Manufacturer'])

'''
A DataFrame is a collection of Series objects, and a single-column DataFrame can be constructed from a single Series:
'''
#Using dictionary to create a series
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
#Creating a DataFrame from car_price Series
car_dataset = pd.DataFrame(car_price, columns=['Car Price'])
print(car_dataset)

'''
From lists of dictionaries
'''
data = [{'Name': 'Subodh', 'Marks': 28},
        {'Name': 'Ram', 'Marks': 27}, 
        {'Name': 'Abdul', 'Marks': 26}, 
        {'Name': 'John', 'Marks': 28}]
data = pd.DataFrame(data)
print(data)

data = pd.DataFrame([{'Subodh':20, 'Ram':25},
              {'Abdul':29, 'John':24}], 
              index = ['Mathematics', 'Physics'])

#Using dictionary to create a series
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
car_man_dict = {'Swift' : 'Maruti',
                  'Jazz'   : 'Honda',
                  'Civic'  : 'Honda',
                  'Altis'  : 'Toyota',
                   'Gallardo' : 'Lamborghini'}
car_man = pd.Series(car_man_dict)
cars = pd.DataFrame({'Price': car_price , 'Manufacturer' : car_man})
print(cars)

'''
The axis keyword
One of the important parameters used while performing operations on DataFrames is 'axis'. Axis takes two values: 0 and 1.

axis = 0 represents row specific operations.

axis = 1 represents column specific operations.
'''