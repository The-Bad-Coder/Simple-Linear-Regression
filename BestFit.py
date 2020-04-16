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

