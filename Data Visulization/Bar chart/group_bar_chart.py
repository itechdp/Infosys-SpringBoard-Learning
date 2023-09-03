import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# Group bar char is showing the vertical bars beside eachother for multiple features
cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

cars_df[
    "DriveTrain"].unique()
grouped_cars = cars_df[["MPG.city","MPG.highway","RPM","DriveTrain"]].groupby(by="DriveTrain").mean().T

fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(7)

grouped_cars.loc['RPM'] /= 100
width=0.2	# We assign the value of the width of the bar and on the number of groups.
ind=list(range(len(cars_df['DriveTrain'].unique()))) 

plt.bar([i for i in ind], height=grouped_cars["4WD"], label="4WD", width=width)
plt.bar([i+width for i in ind], height=grouped_cars["Front"], width=width, bottom=0, label="Front")
plt.bar([i+width*2 for i in ind], height=grouped_cars["Rear"], label="Rear", width=width, bottom=0)

plt.suptitle("Mileage in city, Mileage on highway,RPM vs DriveTrain", fontsize=16)
plt.xlabel("Mileage in city, Mileage in highway, RPM")
plt.ylabel("Average per DriveTrain type")
plt.xticks([i+width for i in ind],["Mileage in City","Mileage in Highway","RPM"])
plt.legend()