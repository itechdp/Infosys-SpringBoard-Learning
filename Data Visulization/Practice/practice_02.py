import matplotlib.pyplot as plt
import pandas as pd

#Visualise the distribution of values for credit card limit and average purchase made on the card. Also, identify the outliers in the data, if any. 

Dataset = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Practice\\CreditCard_DV.csv")

fig,(ax1,ax2) = plt.subplots(2,1)
fig.set_figheight(7)
fig.set_figwidth(10)

ax1.boxplot(Dataset['Credit_Limit'],vert=False)
ax2.boxplot(Dataset['Avg_Purchase'],vert=False)

ax1.set_title("Credit Limit")
ax1.set_xlabel("Credit Limit")
ax2.set_title("Average Purchase")
ax2.set_xlabel("Average Purchase")
fig.tight_layout()
plt.show()
