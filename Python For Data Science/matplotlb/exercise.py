import numpy as np 
import matplotlib.pyplot as plt
x = np.arange(0.0,5.0,0.1)
y = np.cos(2*np.pi*x)*np.exp(-x)

figure = plt.figure(figsize=(5.0,5.0))
ax = figure.add_axes([0,0,1,1])
ax.plot(x,y,color='black',marker='o',markerfacecolor='cyan')
plt.text(1,0.4,'Theta = 60',va = 'center')
plt.annotate('2nd Crest', xy=(2, 0.142), xytext=(2.500, 0.214),arrowprops=dict(facecolor='green',shrink=.01))
ax.set_title("Main Heading")
ax.set_xlabel("Abscissa")
ax.set_ylabel('Ordinate')
ax.grid()

plt.show()