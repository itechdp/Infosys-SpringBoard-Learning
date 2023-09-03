import matplotlib.pyplot as plt
import pandas as pd

# Plot the frequency distribution of the total transaction amount.
Dataset = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Practice\\CreditCard_DV.csv")
Dataset['Total_Trans_Amt'].plot(kind='hist',bins=6,grid=True,figsize=(10,7))
plt.title("Total Transaction Amount")
plt.xlabel("Total Transaction Amount")
plt.show()