import matplotlib.pyplot as plt
import pandas as pd

# Graphically represent the percentage of customers retained and those attrited. Highlight the latter by slicing it apart from the main pie.
Dataset = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Practice\\CreditCard_DV.csv")
values = Dataset['Attrition_Flag'].value_counts()

fig = plt.figure()
fig.set_figheight(7)
fig.set_figwidth(10)
plt.pie(values,autopct='%1.2f%%',labels=['Existing Customer','Attrited Customer'],explode=[0.0,0.1])
plt.show()