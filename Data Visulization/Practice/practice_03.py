import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#Provide a visual representation of the number of customers in each income group using a bar chart.

Dataset = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Practice\\CreditCard_DV.csv")
Dataset['Income_Category'].unique()
plt.bar(x=Dataset['Customer_Age'],height=Dataset['Income_Category'])
plt.show()
