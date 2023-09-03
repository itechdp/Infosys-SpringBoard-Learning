"""
A python List can be used to store a group of elements together in a sequence. It can contain heterogeneous elements.

Following are some examples of List:
"""

item_list = ['Bread', 'Milk', 'Eggs', 'Butter', 'Cocoa']
student_marks = [78, 47, 96, 55, 34]
hetero_list =  [ 1,2,3.0,"text", True, 3+2j ]

'''
To perform operations on the List elements, one needs to iterate through the List. For example, if five extra marks need to be awarded to all the entries in the student marks list. The following approach can be used to achieve the same:
'''

student_marks = [78, 47, 96, 55, 34]
for i in range(len(student_marks)):
    student_marks[i]+=5
print(student_marks)

'''
It can be observed that, there is use of a loop. The code is lengthy and becomes computationally expensive with increase in the size of the List.

Data Science is a field that utilizes scientific methods and algorithms to generate insights from the data. These insights can then be made actionable and applied across a broad range of application domains. Data Science deals with large datatsets. Operating on such data with lists and loops is time consuming and computationally expensive. 
'''

# Creation of numpy array

'''
Syntax:  np.array(object, dtype)
object : A python object(for example, a list)
dtype : data type of object (for example, integer)
'''
import numpy as np
student_marks_arr = np.array([78, 92, 36, 64, 89])
student_marks_arr

'''
Let us understand why Python Lists can become a bottleneck if they are used for large data.
Consider that 1 million numbers must be added from two different lists. 
'''

#Used to calculate total operation time
list1 = list(range(1,1000000))
list2 = list(range(2,1000001))
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print(list1,list2)
'''
Note: Time taken will be different in different systems.
Let us understand, how Numpy can solve the same in minimal time.
Note: Ignore the syntax and focus on only the output.
'''

#Used to calculate total operation time
#Importing Numpy
import numpy as np
#Creating a numpy array of 1 million numbers
a = np.arange(1,1000000)
b = np.arange(2,1000001)
c = a+b
print(a,b)

'''
It can be observed that the same operation has been completed in 12 milliseconds when compared to 395 milliseconds taken by Python List. As the data size and the complexity of operations increases, the difference between the performance of Numpy and Python Lists broadens.
'''



'''
There are various columns in this dataset. Each column contains multiple values. These values can be represented as lists of items. Since each column contains homogenous values, Numpy arrays can be used to represent them.

Let us understand , how to represent the car ‘horsepower’ values in a Numpy array.
'''

#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
print(horsepower_arr)

'''
How can multiple columns be represented together?
This can be achieved by creating the Numpy array from List of Lists.

Let us understand , how to represent the car 'mpg', ‘horsepower’, and 'acceleration' values in a Numpy array.

'''
#creating a list of lists of 5 mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#creating a numpy array from car_attributes list
car_attributes_arr = np.array(car_attributes)
print(car_attributes_arr)

'''
The numpy.ndarray.shape returns a tuple that describes the shape of the array.

For example:

a one-dimensional array having 10 elements will have a shape as (10,)
a two-dimensional array having 10 elements distributed evenly in two rows will have a shape as (2,5)
Let us comprehend, how to find out the shape of car attributes array.
'''
#creating a list of lists of  mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#creating a numpy array from attributes list
car_attributes_arr = np.array(car_attributes)
print(car_attributes_arr.shape)


'''
'dtype' refers to the data type of the data contained by the array. Numpy supports multiple datatypes like integer, float, string, boolean etc.

Below is an example of using dtype property to identify the data type of elements in an array.
'''

#creating a list of lists of 5 mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#creating a numpy array from attributes list
car_attributes_arr = np.array(car_attributes)
print(car_attributes_arr.dtype)

'''
Changing dtype 
Numpy dtype can be changed as per requirements. For example, an array of integers can be converted to float.

Below is an example of using dtype as an argument of np.array() function to convert the data type of elements from integer to float.
'''

#creating a list of lists of 5 mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#converting dtype
car_attributes_arr = np.array(car_attributes, dtype = 'float')
print(car_attributes_arr)
print(car_attributes_arr.dtype)
