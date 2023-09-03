import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mnist_data = pd.read_csv("E:\Programming languages\Python\Infosys SpringBoard\Machine Learning\Clustering\mnist_data.csv")
im = np.array(mnist_data.iloc[0:1,:]).reshape(28,28)

# Building K Means model with 10 cluseters
from sklearn.cluster import KMeans
model = KMeans(n_clusters=10)
model.fit(mnist_data)

# Take a look at the cluster labels that are generated
# Note that these cluster labels do not indicate the digit in the images
print(model.labels_)
print(np.unique(model.labels_))

# Explore images in cluster 1
# cluster1 variable holds the data that has been grouped into the first cluste
cluster1 = mnist_data[model.labels_==0]

# Pick 5 random images from cluster 1
cluster1_images = cluster1.iloc[[np.random.randint(0,cluster1.shape[0]) for i in range(0,5)]]

# Plot the images in cluster 1
for i in range(0,cluster1_images.shape[0]):
    plt.subplot(1,5,i+1)
    img_fig = np.asarray(cluster1_images[i:i+1]).reshape(28,28)
    plt.imshow(img_fig,cmap=plt.cm.gray)

# Explore images in cluster 2
cluster2 = mnist_data[model.labels_==1]
cluster2_imgs = cluster2.iloc[[np.random.randint(0,cluster2.shape[0]) for i in range(0,5)]]
for i in range(0,cluster2_imgs.shape[0]):
    plt.subplot(1,5,i+1)
    img_fig = np.asarray(cluster2_imgs[i:i+1]).reshape(28,28)
    plt.imshow(img_fig,cmap=plt.cm.gray)
