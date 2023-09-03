import pandas as pd
import numpy as np
PATH = r'E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv'
df = pd.read_csv(PATH)

# Pandas also provides us options to visualize the data. Here are some of the examples:

# Syntax:

#        df.plot(X, y, marker, kind)

#        X = value on X axis

#        y = value on y axis

#        marker = shape in case of specific plots like a scatter plot

#        kind = type of plot

# A scatter plot to visualize the trend of acceleration in different years.

df.plot(x = 'model_year', y = 'acceleration', marker = 'o', kind = 'scatter');
df.groupby('model_year').mean()[['acceleration']].plot(kind = 'bar');
df['cylinders'].plot(kind = 'hist')
df.plot(x = 'weight', y = 'mpg', kind = 'scatter')
df.groupby('cylinders').mean().sort_values('acceleration')[['acceleration']].plot(kind = 'bar')
