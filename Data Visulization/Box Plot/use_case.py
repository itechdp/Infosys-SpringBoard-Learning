# Let us consider a use case, where a cutomer wishes to buy a car. Following are some of the questions that the customer might have before the purchase.
# What is the price range of different cars available in the market?
# What is the range of horsepower and mileage of various cars?
# Does a car with higher horsepower give lower mileage?
# How much leg space does the car have?
# How many passengers can the car carry based on its type?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]
cars_df[columns].head()