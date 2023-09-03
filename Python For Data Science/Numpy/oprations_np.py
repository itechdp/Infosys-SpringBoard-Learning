'''
The elements in the ndarray are accessed using index within the square brackets [ ]. In Numpy, both positive and negative indices can be used to access elements in the ndarray. Positive indices start from the beginning of the array, while negative indices start from the end of the array. Array indexing starts from 0 in positive indexing and from -1 in negative indexing.
'''
import numpy as np
#creating an array of cars
cars = np.array(['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino'])
#accessing the second car from the array
print(cars[1])

'''
Accessing elements from a 2D array
'''
#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
print(car_hp_arr)

#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
#Accessing car names
print(car_hp_arr[0])

#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
#Accessing horsepower
print(car_hp_arr[1])

#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
#Accessing second car - 0 represents 1st row and 1 represents 2nd element of the row
print(car_hp_arr[0,1])

#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
#Accessing name of last car using negative indexing
print(car_hp_arr[0,-1])


'''
Slicing is a way to access and obtain subsets of ndarray in Numpy. 
Syntax:   array_name[start : end] – index starts at ‘start’ and ends at ‘end - 1’.
'''

# Slicing from 1D array
#creating an array of cars
cars = np.array(['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino'])
#accessing a subset of cars from the array
print(cars[1:4])

# Slicing from a 2D array
#Creating a 2D array consisting car names, horsepower and acceleration
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
acceleration = [18, 15, 18, 16, 17]
car_hp_acc_arr = np.array([car_names, horsepower, acceleration])
print(car_hp_acc_arr)

#Creating a 2D array consisting car names, horsepower and acceleration
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
acceleration = [18, 15, 18, 16, 17]
car_hp_acc_arr = np.array([car_names, horsepower, acceleration])
#Accessing name and horsepower 
print(car_hp_acc_arr[0:2])

#Creating a 2D array consisting car names, horsepower and acceleration
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
acceleration = [18, 15, 18, 16, 17]
car_hp_acc_arr = np.array([car_names, horsepower, acceleration])
#Accessing name and horsepower of last two cars 
print(car_hp_acc_arr[0:2, 3:5])

#Creating a 2D array consisting car names, horsepower and acceleration
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
acceleration = [18, 15, 18, 16, 17]
car_hp_acc_arr = np.array([car_names, horsepower, acceleration])
#Accessing name, horsepower and acceleration of first three cars
print(car_hp_acc_arr[0:3, 0:3])
