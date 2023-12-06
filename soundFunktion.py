import numpy as np
import matplotlib.pyplot as plt


data1 = []
data2 = []
with open("lungs3_0.txt", 'r') as f:
    for line in f.readlines():
        data1.append(int(line.strip()))   
with open("lungs3_1.txt", 'r') as f:
    for line in f.readlines():
        data2.append(int(line.strip())) 
data1 = np.array(data1)
data2 = np.array(data2)

plt.plot(np.arange(len(data1)), (data1 - np.sum(data1)/len(data1))/max(data1))
plt.plot(np.arange(len(data2)), (data2 - np.sum(data2)/len(data2))/max(data2))
# plt.plot(np.arange(len(data2)), data2/max(data2))
plt.show()