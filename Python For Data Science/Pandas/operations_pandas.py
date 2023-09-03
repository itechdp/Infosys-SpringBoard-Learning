import pandas as pd
import numpy as np
PATH = r'E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv'
df = pd.read_csv(PATH)

#  Problem statement : Retrieve details of all the cars built in year 72.

print(df.loc[df['model_year'] == 72].head())

# Problem statement : Retrieve details of all the cars built in Japan having 6 cylinders
print(df.loc[(df['origin'] == 'japan') & (df['cylinders'] == 6)])

# Fuel efficient
# MPG > 29 , Horsepower < 93.5
# Weight < 2500

fuel_eff = df.loc[(df['mpg'] > 29) & (df['horsepower'] < 93.5) & (df['weight'] < 2500)]

# Muslce Cars
# Displacement > 262 , Horsepower > 126 , Weight in range[2800,3600]

muscle_car = df.loc[(df['displacement'] > 262) & (df['horsepower'] > 126) & (df['weight'] >= 2800) & (df['weight']<=3600 )]

# SUV 
# Horsepower >140 , weight > 4500
suv_car = df.loc[(df['horsepower'] > 140) & (df['weight'] >= 4500)]

# Racecar
# Weight <2223, acceleration > 17
race_car = df.loc[(df['acceleration'] > 17) & (df['weight'] < 2223)]

#Problem Statement:
#The teacher does not want to reveal the marks of students who have failed. The condition is that if a student has scored marks >= 33, then they have passed, otherwise failed. The marks of failed students has to be replaced with ‘Fail’. So, how can the task be performed?.

marks = [
    {'Chemistry':67,'Physics':45,'Maths':50,"English":19},
    {'Chemistry':90,'Physics':92,'Maths':87,"English":72},
    {'Chemistry':66,'Physics':72,'Maths':81,"English":90},
    {'Chemistry':32,'Physics':40,'Maths':12,"English":68},   
         ]

marks_df = pd.DataFrame(marks,index=['Subodh','Ram','Abdul','John'])
print(marks_df)

'''
Syntax:

       DataFrame.mask(cond, other = nan, inplace = False, axis = None)

       cond – Where cond is False, keep the original value. Where True, replace with corresponding value from other

       other - Entries where cond is True are replaced with corresponding value from other.

       inplace - Whether to perform the operation in place on the data.

       axis – alignment axis
'''

f = marks_df < 33
marks_df = marks_df.mask(f,"Fail")
print(marks_df)

#Problem Statement:
#XYZ Custom cars want the data sorted according to the number of cylinders. 

cylinder_sort = df.sort_values(by='cylinders')

#Problem Statement:
#There is a requirement in which the cars that have lowest acceleration must be assessed. It is also to be checked that which cars have higher horsepower despite having lower acceleration.

horse_sort = df.sort_values(['acceleration','horsepower'],ascending=(1,0))


#Problem Statement:
#The teacher wants to encrypt the marks for confidential reasons. Therefore, the teacher decides to save the marks as sine of the original marks. For example, if Subodh has scored 67 in chemistry, then his encrypted marks will be sin(67) = -0.855520

marks = {'Chemistry': [67,90,66,32], 
        'Physics': [45,92,72,40],  
        'Mathematics': [50,87,81,12],  
        'English': [19,90,72,68]}

marks_df = pd.DataFrame(marks,index=['Subodh','Ram',"Abdul","John"])
encrypted_marks = np.sin(marks_df)
print(encrypted_marks)

# Restting the index
encrypted_marks.reset_index(inplace=True)
print(encrypted_marks)

#Problem Statement:
#The teacher wants to award five bonus marks to all the students.
new_marks = marks_df + 5
print(new_marks)

#Problem Statement:
#The teacher wants to increase the marks of all the students as follows-
#
#Chemistry: + 5
#
#Physics: + 10
#
#Mathematics: +10
#
#English: + 2

new_marks = marks_df + [5,10,10,2]
print(new_marks)

#Apply
#This method is used to apply a function along an axis of the DataFrame.
#
#Syntax:
#
#       DataFrame.apply(func, axis = 0, result_type = None)
#
#       func : Function to apply to each column or row.
#
#       axis: Axis along which the function is applied.
#
#       result_type: one out of 'expand', 'reduce' or 'broadcast'. In the demo, 'broadcast' is used.
#
#‘broadcast’ : results will be broadcast to the original shape of the DataFrame, the original index and columns will be retained.

#Creating the DataFrame
marks = {'Chemistry': [67,90,66,32], 
        'Physics': [45,92,72,40],  
        'Mathematics': [50,87,81,12],  
        'English': [19,90,72,68]}
marks_df = pd.DataFrame(marks, index = ['James', 'Lee', 'Anderson', 'John'])

#Problem statement : 
#The teacher wants to get the total marks scored in each subject

marks_df.apply(np.sum,axis=0)

#Problem statement: 
#The teacher wants to get the total marks scored by each student.

marks_df.apply(np.sum,axis=1)

#Problem Statement:
#The students were unable to attend the next set of exams due to the pandemic. Hence, the teacher decides to award them average marks based on their previous performance.

marks_df.apply(np.mean,axis=0,result_type='broadcast')

#Problem Statement:
#Consider the scenario where the board of XYZ custom cars wants to know about minimum and maximum of all the numerical columns.

#Solution:
#Aggregation operation is used to aggregate using one or more operations over the specified axis.
#
#Syntax:
#
#DataFrame.agg(func, axis = 0)
#
#func - Function to use for aggregating the data. If a function, must either work when passed a DataFrame or when  passed to DataFrame.apply.
#
#axis: If 0 or ‘index’: apply function to each column. If 1 or ‘columns’: apply function to each row.
#
#The below code is used to find minimum and maximum values of the numerical attributes:

#Using list comprehension to get the numerical columns
list1 = [col for col in df.columns if df[col].dtype in ['float', 'int64']]
df[list1].agg['min','max']

#XYZ custom cars want to know the number of cars manufactured in each year.
#This would require a grouping operation. Pandas supports a group by feature to group our data for aggregate operations.

#Syntax:

#       DataFrame.groupby(by = column_name, axis, sort)
#
#Problem statement:
#How many cars belong to each year?

df.groupby(['model_year']).count()[['name']]

#Problem Statement: 
#Some senior engineers in XYZ custom cars want to understand about the effect of model year and number of cylinders on horsepower.

#Creating a DataFrame grouped on cylinders and model_year and finding mean, min and max of horsepower
grouped_multiple = df.groupby(['cylinders', 'model_year']).agg({'horsepower': ['mean', 'min', 'max']})
#Naming columns in grouped DataFrame
grouped_multiple.columns = ['hp_mean', 'hp_min', 'hp_max']
#Resetting index
grouped_multiple = grouped_multiple.reset_index()
#Viewing head of resulting DataFrame
grouped_multiple.head()

# Problem statement: 
# The engineers at XYZ Custom Cars want to know about the relationship between model year and acceleration of cars.

df.groupby(['model_year']).mean().sort_values('acceleration', ascending = False)[['acceleration']]

marks_A = {'Chemistry': [67,90,66,32], 
        'Physics': [45,92,72,40],  
          }
marks_A_df = pd.DataFrame(marks_A, index = ['Subodh', 'Ram', 'Abdul', 'John'])
marks_B = {'Chemistry': [72,45,60,98], 
        'Physics': [78,34,72,95],  
          }
marks_B_df = pd.DataFrame(marks_B, index = ['Nandini', 'Zoya', 'Shivam', 'James'])

#Problem Statement:
#The teacher wants to combine the marks of these students

pd.concat([marks_A_df,marks_B_df], sort = False)

df1 = pd.DataFrame({'employee': ['Jyoti', 'Sapna', 'Raj', 'Ramaswamy'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Jyoti', 'Sapna', 'Raj', 'Ramaswamy'],
                    'hire_date': [2004, 2008, 2012, 2014]})

pd.concat([df1,df2], sort = False)

#Using Merge in case of column mismatch
#To resolve the above condition, the merge function can be used which joins two tables based on a key. 
df3 = pd.merge(df1,df2)

#Problem statement: 
#The engineers at XYZ Custom Cars want to know the frequency distribution of different number of cylinders across different years.

pd.crosstab(df['model_year'], df['cylinders'])

#A Pivot Table is used to summarise, sort, reorganise, group, count, total or average data stored in a table. If we want to create spreadsheet-style pivot table as a data frame, pandas provides us with an option.

#Problem Statement:
#The engineers at XYZ custom cars want to know the mean of all the numerical attributes of cars for each year

#Syntax :
#       pd.pivot_table(data, index, aggfunc)

#      data: DataFrame

#      index: column to be set as index

#       aggfunc: function/list of functions, default = numpy.mean

pivot1 = pd.pivot_table(df, index = 'model_year', aggfunc=np.mean)
