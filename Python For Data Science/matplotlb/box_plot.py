import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH = r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv"
df = pd.read_csv(PATH)
df.info() #to know the column names, missing values and their data type

# replacing the null values in horsepower with its mean
df['horsepower'].fillna(df['horsepower'].mean(),inplace=True)

# A boxplot gives a good indication of distribution of data about the median. Boxplots are a standardized way of displaying the distribution of data based on the five-number summary (“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”).


#Problem Statement:
#Some customers of XYZ Custom Cars are interested in the mileage range of the cars that are restored by the company. They also want to compare the distribution of average mileage and city mileage (25% less than the average mileage). 

#Solution:
#First, let us plot the average mileage ‘mpg’ from the data using a boxplot.

#Syntax:
#ax.boxplot(data)  #ax represents axes

# Creating an empty canvas
fig = plt.figure(figsize=[6,6])

# Setting axes
ax = fig.add_axes([0,0,1,1])
ax.set_title("Distribution of mileaage")

# Pltting box plot
ax.boxplot(df['mpg'])

#There is no data for city mileage, but city mileage is 25% less than the average mileage i.e. ‘mpg’. Next is to process the data for city mileage.

#Processing data for city mileage
df['city_mileage'] = df['mpg']*0.75
print(df.head())

#A new column  ‘city_mileage’ is created . Next, the distribution of the average mileage and city mileage has to be compared.

mpg_list = [df['mpg'],df['city_mileage']]
print(mpg_list)

#creating an empty canvas/figure
fig = plt.figure(figsize=[6,5])
#setting axes
ax = fig.add_axes([0, 0, 1, 1])

ax.set_title('Distribution of Average MPG vs City MPG')
ax.set_ylabel('Mileage per gallon')
#plotting box plot
ax.boxplot(mpg_list,widths = 0.5)
plt.show()
