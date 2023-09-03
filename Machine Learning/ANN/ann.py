import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Train data contains digit data and the correct labels
# Test data contains just the digit data and no labels 

mnist_train = pd.read_csv("E:\Programming languages\Python\Infosys SpringBoard\Machine Learning\Clustering\mnist_data.csv")
mnist_test = pd.read_csv("E:\Programming languages\Python\Infosys SpringBoard\Machine Learning\Clustering\mnist_data.csv")

# Let's visualize the image represented by the first rows of the train data and the test data
train_data_digit1 = np.asarray(mnist_train.iloc[0:1,1:]).reshape(28,28)
test_data_digit1 = np.asarray(mnist_test.iloc[0:1,]).reshape(28,28)

plt.subplot(1,2,1)
plt.imshow(train_data_digit1,cmap = plt.cm.gray_r)
plt.title("First digit in train data")
plt.subplot(1,2,2)
plt.imshow(test_data_digit1,cmap = plt.cm.gray_r)
plt.title("First digit in test data ")

"""Let us now assign the label column value to a new variable Y_train 
and the remaining column values to X_train"""
X_train = mnist_train.iloc[:,1:]
Y_train = mnist_train.iloc[:,0:1]

from sklearn.neural_network import MLPClassifier
# Let us now create a neural network model to learn from train data
# We shall build a single hidden layer with 50 nodes. 
nn_model = MLPClassifier(hidden_layer_sizes=(50))
# The fit method initiates the learning process. When its execution completes, the model is learnt
nn_model.fit(X_train,mnist_train.iloc[:,0])
# Now that we have a model, lets get it to predict the value of the first digit in the test data
print(nn_model.predict(mnist_test.iloc[0:1,]))
# output
# [2]
