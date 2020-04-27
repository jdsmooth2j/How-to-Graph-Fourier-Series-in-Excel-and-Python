#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing numpy anf matplotlib modules
import numpy as np
import matplotlib.pyplot as plt

#Plot Style
plt.style.use("ggplot")


# In[32]:


#Defining and Plotting the Square Wave Function and Evaluating its Approximations
#The parameters we need to approximate a function with Fourier Series
    #1) A periodic bounded function, with period T
    #2) The function should be integrable over the period

#If the above conditions are met, then we can define the function as follows (see attached Fourier Series equation)
from PIL import Image
img  = Image.open("Desktop/Fourier Series Equation.jpg","r")
img.show()

# Specifying interval
x_ = np.linspace(-10,10,10000)

#Period T and nth harmonics
T = 10
nth = 15

#Note: to fine tune the approximation or to make the approximation FINER 'increase nth'

#Defining the Square Wave Function
def SquareWave(x):
    global T
    lowerBoundLeft = (-T/2)
    lowerBoundRight = 0
    upperBoundLeft = 0
    upperBoundRight = (T/2)
    one = 1
    negativeOne = -1

    while True:
        if (x >= lowerBoundLeft) and (x <= lowerBoundRight):
            return negativeOne
        elif (x >= upperBoundLeft) and (x <= upperBoundRight):
            return one
        else:
            lowerBoundLeft -= T/2
            lowerBoundRight -= T/2
            upperBoundLeft += T/2
            upperBoundRight += T/2
            if one == 1:
                one = -1
                negativeOne = 1
            else:
                one = 1
                negativeOne = -1

# evaluate bn coefficients
def bn(n):
    n = int(n)
    if (n%2 != 0):
        return 4/(np.pi*n)
    else:
        return 0

#let ωn = 2πn/T
def wn(n):
    global T
    wn = (2*np.pi*n)/T
    return wn

# Defining Fourier Series Function
def fFourierSeries(n_max,x):
    a0 = 0
    partialSums = a0
    for n in range(1,n_max):
        try:
            partialSums = partialSums + bn(n)*np.sin(wn(n)*x)
        except:
            print("pass")
            pass
    return partialSums


y = []
f = []
for i in x_:
    y.append(squareWave(i))
    f.append(fourierSeries(nth,i))

    
#Plotting the Square Wave Input and its Approximation

#labeling functions
plt.plot(x_,y,color="blue",label="Square Wave Input")
plt.plot(x_,f,color="red",label="Square Wave Approximation")

#Provide title
plt.title("Square Wave Approximation Number of Harmonics: "+str(nth))

# Provide x axis label
plt.xlabel('Time')

# Provide y axis label
plt.ylabel('Amplitude')

#Grid Style
plt.grid(True, which='both', linestyle='-.')

# Provide x axis and line color
plt.axhline(y=0, color='k')

#Show graph
plt.show()


# In[31]:


#Useful insights and References
#https://en.wikipedia.org/wiki/Fourier_series
#https://en.wikipedia.org/wiki/Square_wave
#https://mathworld.wolfram.com/FourierSeries.html

#If you have time, perhaps you could try plotting Triangular, Sawtooth Wave, Half- and Full-Wave Rectified Sine Waves.
#Sample Output for Sawtooth Wave Simulation
from PIL import Image
img  = Image.open("Desktop/Sawtooth Wave Simulation.png","r")
img.show()


# In[ ]:




