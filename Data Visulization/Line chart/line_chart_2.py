import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

# Sorting the data for line chart
cars_df = cars_df.sort_values(by="Horsepower")

fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(7)

plt.plot(cars_df['Horsepower'],cars_df['MPG.city'],label='MPG.city')
plt.plot(cars_df['Horsepower'],cars_df['Engine Size'],label="Engine Size")
plt.plot(cars_df['Horsepower'],cars_df['MPG.highway'],label="MPG.highway")
plt.plot(cars_df['Horsepower'],[i/100 for i in cars_df['RPM']],label='RPM')
plt.suptitle("Horsepower vs Mileage in city, Engine Size, Mileage on highway, RPM")
plt.xlabel("Horsepower")
plt.ylabel("Mileage in city,Engine size, Mileage on highway, RPM")
plt.legend()
