import math 
import matplotlib.pyplot as plt
import numpy as np

M = (2 * np.pi) / 3
K = (2*np.pi)/(3*np.sqrt(3)) 

x1 = np.linspace(0, M) 
x2 = np.linspace(-K, K)
x3 = np.linspace(-M, 0)


#from Gamma to K points 
y_p = 3 * (1 + (np.sqrt(1 + 4 * np.cos(1.5 * x1) * np.cos(0.5 * x1) + 4 * np.power(np.cos(0.5*x1), 2)))/3)
y_n = 3 * (1 - (np.sqrt(1 + 4 * np.cos(1.5 * x1) * np.cos(0.5 * x1) + 4 * np.power(np.cos(0.5*x1), 2)))/3)

#from K to -K points path 
y2_p = 3 * (1+ ((1 - 2*np.cos( (np.sqrt(3)/2) *x2)))/3)
y2_n = 3 * (1- ((1 - 2*np.cos( (np.sqrt(3)/2) *x2)))/3)

#from -K to Gamma points 
y3_p = 3 * (1 + (np.sqrt(1 + 4 * np.cos(1.5 * x3) * np.cos(0.5 * x3) + 4 * np.power(np.cos(0.5*x3), 2)))/3)
y3_n = 3 * (1 - (np.sqrt(1 + 4 * np.cos(1.5 * x3) * np.cos(0.5 * x3) + 4 * np.power(np.cos(0.5*x3), 2)))/3)

plt.plot(x1, y_p, "r")
plt.plot(x1, y_n, "b")

plt.plot(x2+K+M, y2_p, "r")
plt.plot(x2+K+M, y2_n, "b")

plt.plot(x3+2*K+2*M, y3_p, "r")
plt.plot(x3+2*K+2*M, y3_n, "b")
plt.show()