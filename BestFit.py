import numpy as np
import matplotlib.pyplot as plt

def SlopeIntercept(x,y):
    global meanX , meanY , m1 , c , m , c
    meanX = np.mean(x)
    meanY = np.mean(y)
    Sy = np.sum( (x - meanX)*(y - meanY) )
    Sx = np.sum( (x - meanX)**2 )
    m = Sy /Sx
    c = meanY - m*meanX


def plot():
    global m , c , x , y 
    plt.scatter(x , y , color = 'c', marker = 'd')
    Y = np.array(m*x  + c)
    plt.plot(x , Y , 'r:')
    plt.show()

x = np.array([1,2,3,4,5,6])
y = np.array([3,4,2,4,5,7])
SlopeIntercept(x,y)
plot()