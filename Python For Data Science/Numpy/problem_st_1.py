
'''
Problem Statement:
The engineers at XYZ Custom Cars want to know about the mean and median of horsepower. 

Solution:
'''
import numpy as np
#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#mean horsepower
print("Mean horsepower = ",np.mean(horsepower_arr))

#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#median horsepower
print("Median horsepower = ",np.median(horsepower_arr))

'''Problem Statement: 
The engineers at XYZ Custom Cars want to know about the minimum and maximum horsepower.

Solution:
The min and max can be calculated with the help of following code:
'''
#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
print("Minimum horsepower: ", np.min(horsepower_arr))
print("Maximum horsepower: ", np.max(horsepower_arr))

'''
Finding the index of minimum and maximum values:
'argmin()' and 'argmax()' return the index of minimum and maximum values in an array respectively.
'''
#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
print("Index of Minimum horsepower: ", np.argmin(horsepower_arr))
print("Index of Maximum horsepower: ", np.argmax(horsepower_arr))

'''
Problem Statement: 
The engineers at XYZ Custom Cars want to know the horsepower of cars that are greater than or equal to 150.

Solution:
The 'where' function can be used for this requirement. Given a condition, 'where' function returns the indexes of the array where the condition satisfies. Using these indexes, the respective values from the array can be obtained.
'''

#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
x = np.where(horsepower_arr >= 150)
print(x) # gives the indices 
# With the indices , we can find those values 
print(horsepower_arr[x])

'''
Problem Statement:
The Engineers at XYZ Custom Cars want to create a separate array consisting of filtered values of horsepower greater than 135.

Solution:
Getting some elements out of an existing array based on certain conditions and creating a new array out of them is called filtering.

The following code can be used to accomplish this:
'''

#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#creating filter array
filter_arr = horsepower_arr > 135
newarr = horsepower_arr[filter_arr]
print(filter_arr)
print(newarr)

'''
Problem Statement:
The engineers at XYZ Custom Cars want the horsepower in sorted order.

Solution:
The  numpy array can be sorted by passing the array to the function sort(array) or by array.sort.

So, what is the difference between these two functions though they are used for the same functionality?
'''

#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#using sort(array)
print('original array: ', horsepower_arr)
print('Sorted array: ', np.sort(horsepower_arr))
print('original array after sorting: ', horsepower_arr)

#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#using sort(array)
print('original array: ', horsepower_arr)
horsepower_arr.sort()
print('original array after sorting: ', horsepower_arr)

'''
The difference is that the array.sort() function modifies the original array by default, whereas the sort(array) function does not.
'''

'''
Problem Statement:
Calculate the sum of all the marks.

Solution:
The sum() function can be used which internally uses vectorizaton .
'''
student_marks_arr = np.array([78, 92, 36, 64, 89])
print(np.sum(student_marks_arr))

'''
Problem Statement:
Award extra marks in subjects as follows:

English: +2

Mathematics: +2

Physics: +5

Chemistry: +10

Biology: +2

Solution:
Below is the solution to the problem:
'''
additional_marks = [2, 2, 5, 10, 1]
student_marks_arr += additional_marks
student_marks_arr

'''
Also, the same operation can be performed as shown below:
'''


student_marks_arr = np.array([78, 92, 36, 64, 89])
student_marks_arr = np.add(student_marks_arr, additional_marks)

'''
Broadcasting" refers to the term on how Numpy handles arrays with different shapes during arithmetic operations. Array of smaller size is stretched or copied across the larger array.

For example, considering the following arithmetic operations across 2 arrays:
'''
# Array 1
array1=np.array([5, 10, 15])
# Array 2
array2=np.array([5])
array3= array1 * array2 
array3

'''
Consider the following table
'''
student_marks = np.array([[67,45],[90,92],[66,72],[32,40]])
print(student_marks)

'''
Problem Statement:
Now the teacher wants to award extra five marks in Chemistry and extra ten marks in Physics.

Solution:
'''
#Students marks in 4 subjects
students_marks = np.array([[67, 45],[90, 92],[66, 72],[32, 40]])
#Broadcasting
students_marks += [5,10]
print(student_marks)