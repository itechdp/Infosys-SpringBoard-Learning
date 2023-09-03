import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# Histogram 

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")
columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

# Histogram is helping us to see the frequency on the numerical data
# Consider we are trying to find the mileage freqency of all the total number of cars 

#The 'kind = density' parameter plots the density line of the data. The 'density = True' parameter returns the probability densities of each bar of the histogram. And, the xlim( ) method is used to set the limit of the axis between 14 and 50, as shown in the code below:

cars_df["MPG.city"].plot(kind='density')
cars_df['MPG.city'].plot(kind='hist',density=True,grid=True,figsize=(10,7),bins=6,color='C1')
plt.suptitle("Distribution of MPG.city")
plt.xlim((13,50)) # Giving custom values to X Axis
plt.legend()

# Output will shows us that the most of cars are giving mileage of 15 to 20
plt.show()