#importing the required packages
import matplotlib.pyplot as plt
import pandas as pd
PATH = r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv"
df = pd.read_csv(PATH)

line_df = df.groupby(by=['model_year'])
line_df = line_df.mean()

#creating an empty canvas/figure
fig = plt.figure(figsize=[10,5])
#setting axes
ax = fig.add_axes([0, 0, 1, 1])
#plotting the lines
ax.plot(line_df['mpg']/10,label='Mileage')
ax.plot(line_df['weight']/1000,label='Weight')
ax.plot(line_df['horsepower']/100,label='Horsepower')

plt.text(75.5, 1.14, 'Horsepower',
             va = 'center', #va -> vertical alignment
             rotation = 4, #angle
             bbox = dict( 
                     boxstyle = 'round',
                     facecolor = 'wheat',
                     alpha = 0.3)) #background style

plt.text(75.5, 2.25, 'Mileage',va = 'center',rotation = 17,bbox = dict(boxstyle = 'round',facecolor = 'wheat',alpha = 0.3))
plt.text(76, 3.15, 'Weight',va = 'center',rotation = -13,bbox = dict(boxstyle = 'round',facecolor = 'wheat',alpha = 0.3))
plt.annotate('Highest Mileage', xy=(80.1, 3.39), xytext=(80.5, 3.38), arrowprops=dict(facecolor='wheat', shrink=.01))
plt.annotate('Lowest Mileage', xy=(73.05, 1.70), xytext=(73.5, 1.69), arrowprops=dict(facecolor='wheat', shrink=.01))


ax.set_title('Mileage vs Weight vs Horsepower',fontsize = 17)
ax.set_ylabel('Value',fontsize=12)
ax.set_xlabel('Model year',fontsize=12)
plt.show()