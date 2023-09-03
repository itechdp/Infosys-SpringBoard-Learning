import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# Group bar char is showing the vertical bars beside eachother for multiple features
cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

# Finding the number of cars based on the number of cylinders
cars_df['Cylinders'].unique()
grouped_data = cars_df[['Cylinders','Type']].groupby(by=['Cylinders','Type']).size().unstack()
fig,ax = plt.subplots(2,3,figsize=(15,10))

grouped_data.plot.pie(ax=ax,subplots=True)
fig.suptitle('Number of cars for each type of cylinders',x=1,y=2.1)
fig.tight_layout(rect=[0,0,2,2])
