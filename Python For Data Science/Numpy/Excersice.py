import numpy as np

day_number = [1,2,3,4,5,6,7,8,9,10]
steps_walked = [6012,7079,6886,7230,4598,5564,6971,7763,8032,9569]
dataset = np.array([day_number,steps_walked])
add_step = [2000]
dataset[1]+=add_step
print(dataset)

x = np.where(dataset>9000)
print(dataset[x])
print(np.sort(dataset[1]))