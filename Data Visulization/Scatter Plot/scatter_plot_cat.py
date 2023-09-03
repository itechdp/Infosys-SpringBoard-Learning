import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]
car_type_list = cars_df['Type'].unique()

fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(7)

colors = cm.seismic_r(np.linspace(0,1,len(car_type_list)))
# extract the colours using the 'seismic_r' method. Here, 'r' indicates the reverse.

for car_type,c in zip(car_type_list,colors): # for every car type in the car_type_list we plot all the points in the scatter plot
    x = cars_df[cars_df['Type']==car_type]['Horsepower']
    y = cars_df[cars_df['Type']==car_type]['MPG.city']
    plt.scatter(x,y,color=c,label=car_type)

plt.suptitle("Scatter plot of horsepower and mileage")
plt.xlabel("Horsepower")
plt.ylabel("Mileage City")
plt.legend()
plt.show()