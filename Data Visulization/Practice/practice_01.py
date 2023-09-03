import matplotlib.pyplot as plt
import pandas as pd

# Create a bivariate plot to find if there is a correlation between credit card limit and average purchase made on the card.
Dataset = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Practice\\CreditCard_DV.csv")
ax = Dataset.plot(x=['Credit_Limit'],y=['Avg_Purchase'],kind='scatter')
ax.set_xlabel("Credit Card Limit")
ax.set_ylabel("Average Purchase")
ax.set_title("Correlations Creadit Card Limit VS Average Purchase")
plt.show()


