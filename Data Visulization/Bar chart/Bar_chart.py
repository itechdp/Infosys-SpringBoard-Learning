import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(7)

# Create a bar chart
plt.bar(cars_df['DriveTrain'],cars_df['MPG.city'],width=0.2,label='Mileage in city')

# Title and label
plt.suptitle("Drive Train vs MPG.city")
plt.xlabel("Drive Train")
plt.ylabel('MPG.city')
plt.legend()

