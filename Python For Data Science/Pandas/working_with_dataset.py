import pandas as pd
import numpy as np
PATH = r'E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv'
df = pd.read_csv(PATH)
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
df.dropna(inplace=True)
df.info()

'''
'inplace' makes changes to the original DataFrame.
df.fillna(condition) can be used to fill all the missing values. The missing values are filled with mean, median, mode, or constant values.

'''
print(df['name'])
print(df[['name']])
print(df[['name','origin','mpg']])

# Setting custon index
df_head = df.head()
# Setting name as custon index
df_head.set_index('name',inplace=True)
print(df_head)

'''
'iloc' and 'loc' are the two indexing techniques that help us in selecting specific rows and columns.
1.      iloc- Access a group of rows and columns by integer index.
The ‘iloc’ indexer follows implicit index.  
Syntax - df.iloc[Rows, Columns]
In the following demos, 'df' refers to XYZ Custom Cars DataFrame.
'''
print(df.iloc[2,1])
print(df.iloc[2,-1])
print(df.iloc[1:5,4:6])

'''
2.loc- Access a group of rows and columns by custom index.
The loc indexer follows explicit indexing.
'''

df_head = df.head()
df_head.set_index('name',inplace=True)
print(df_head.loc['buick skylark 320':'amc rebel sst'])

#Subsetting from the full dataset
print(df.loc[0:5, ['cylinders', 'horsepower', 'name']])

marks = {'Chemistry': [67,90,66,32], 
        'Physics': [45,92,72,40],  
        'Mathematics': [50,87,81,12],  
        'English': [19,90,72,68]}
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])
print(marks_df)
marks_df['Total'] = marks_df['Chemistry'] + marks_df['Physics'] + marks_df['Mathematics'] + marks_df['English']
print(marks_df)
marks_df.drop(columns = 'Total', inplace = True)
