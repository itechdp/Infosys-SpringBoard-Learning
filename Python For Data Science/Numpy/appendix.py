import numpy as np
# Arange
# This method returns evenly spaced values between the given intervals excluding the end limit. The values are generated based on the step value and by default, the step value is 1.
#start and end limit
np.arange(0,10000)
#step value = 2
np.arange(0,10,2)

# Linspace
# This method returns the given number of evenly spaced values, between the given intervals. By default, the number of values between a given interval is 50.
#Generating values between 0 and 10
arr = np.linspace(0,10)
print(arr)
print('Length of arr: ',len(arr))

#Number of values = 3
print(np.linspace(0,10,3))

# Zeros
# Returns an array of given shape filled with zeros.
#1D
np.zeros(5)
#2D
np.zeros([2,3])

# Ones
# Returns an array of given shape filled with ones.
#1D
np.ones(3)
#2D
np.ones([2,1])

# Full:
# Returns an array of given shape, filled with given value, irrespective of datatype.
#number=5, value=8
np.full(5,8)
#shape=[3,3], value=numpy
np.full([3,3],'numpy')
# Eye
# Returns an identity matrix for the given shape.
#3x3 identity matrix
np.eye(3)
# Random
# NumPy has numerous ways to create random number arrays. Random numbers can be created for the required length, from a uniform distribution by just passing the value of required length to the random.rand function.
#generating 5 random numbers from a uniform distribution
np.random.rand(5)

# Note: Output might not be same as it is randomly generated.
# Similarly, to generate random numbers from a Normal distribution, use random.randn function.
# Random numbers of type 'integer' can also be generated using random.randint function. Below shown is an example of creating five random numbers between 1 and 10.
#random integer values low=1, high=10, number of values=5
np.random.randint(1,10, size=5)

# Similarly, two-dimensional arrays of random numbers  can also be created by passing the shape instead of number of values.
#random integer values high=100, shape = (3,5)
x = np.random.randint(100, size=(3, 5))
print(x)
print(type(x))

# To generate a random number from a predefined set of values present in an array, the choice() method can be used.
# The choice() method takes an array as a parameter and randomly returns the values based on the size.
#returns a single random value from the array
x = np.random.choice([9, 3, 7, 5])
print(x)

#returns 3*5 random values from the array
x = np.random.choice([9, 3, 7, 5], size=(3, 5))   # sampling to create an nd-array 
print(x)
print(type(x))

