'''
Images are stored as arrays of hundreds, thousands or even millions of picture elements called as pixels. Therefore, images can also be treated as Numpy array, as they can be represented as matrix of pixels.

Certain basic operations and manipulations can be carried out on images using Numpy and scikit-image package. Scikit-image is an image processing package.

The package is imported as skimage.
'''
#Importing path and skimage i/o library 
import os.path
from skimage import imread
from skimage import data_dir
import numpy as np
#reading the astronaut image
img = imread(os.path.join(data_dir, 'astronaut.png'))

#Using matplotlib.pyplot to visualize the image 
import matplotlib.pyplot as plt
plt.imshow(img)

# To view as a matrix, the below command must be followed:
print(img)

print('Type of image: ', type(img))
print('Dimensions of image: ', img.ndim)
print('Shape of image:', img.shape)


'''
So far, you have become familiar with, how to retrieve the basic attributes of the image. Let us proceed to understand some examples on indexing and selection on images.
'''

#Importing path and skimage i/o library 
#reading the astronaut image
img = imread(os.path.join(data_dir, 'astronaut.png'))
#Slicing out the rocket 
img_slice = img.copy()
img_slice = img_slice[0:300,360:480]
plt.figure()
plt.imshow(img_slice)

'''
In this case, the image has been sliced corresponding to the rocket from the original image.

Assigning the values corresponding to the sliced image as 0:
'''
img[0:300,360:480,:] = 0
plt.imshow(img)

img_slice[np.greater_equal(img_slice[:,:,0],100) & np.less_equal(img_slice[:,:,0],150)] = 0
plt.figure()
plt.imshow(img_slice)

'''
The place where the sliced rocket image was present initially, is now filled with black color because 0 is assigned  to the values corresponding to the sliced image.
'''
img[0:300,360:480,:] = img_slice
plt.imshow(img)
