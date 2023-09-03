import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

# Getting the multiple categories with different colours representing each category

#Use the following code snippet to filter the unique values of no. of passengers a car can carry
cars_df['Passengers'].unique()

#Use the following code snippet to filter the unique values of Types of car.
cars_df['Type'].unique()

grouped_data = cars_df[['Passengers','Type']].groupby(by=["passengers,'Type"]).size().unstack().reset_index()

#Stacked Bar Graph can be plotted using the grouped data, as follows:
grouped_data.plot(x='Passengers',kind='bar',stacked=True,colormap=cm.Paired,figsize=(10,7))
