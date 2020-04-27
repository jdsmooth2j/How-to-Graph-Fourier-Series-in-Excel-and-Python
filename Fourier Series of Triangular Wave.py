#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
plt.get_backend()
'Qt4Agg'
plt.clf()
plt.cla()
plt.close()


# In[62]:


#Triangular Wave Formula
print('f(x)= (8/π^2)*Σ(((-1)^((n-1)/2))/(1/n^2))*sin(nπx/L)) from n=1 to ∞')
print('Note: Period, T = 2L')
print('Data from Excel has a period T=4')

#Open image file for the formula in detail
from PIL import Image
img  = Image.open("Desktop/Triangular Wave.jpg","r")
img.show()


# In[65]:


#Showing Data for the Approximations of the Triangular Wave
FS = pd.read_excel (r'C:\Users\hp\Documents\Downloads\Fourier Series_Waveforms.xlsx', sheet_name='Triangular')
TWA = pd.DataFrame(FS, columns= ['f(x)','f(x)=S1+S2','f(x)=S1+S2+S3','f(x)=S1+S2+S3+S4'])

TWA.head()
TWA


# In[66]:


#Plotting Triangular Wave Approximations from Sums of Sinusoidal Compositions
plt.plot(TWA)
  

# Give a title for the triangular wave plot
plt.title('Triangular Wave Approximations')


# Give x axis label for the triangular wave plot
plt.xlabel('Time Scaled at 1:20ms')


# Give y axis label for the triangular wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both', linestyle='-.')

 
# Provide x axis and line color
plt.axhline(y=0, color='k')

 
# Set the max and min values for y axis
plt.ylim(-1.5, 1.5)

#Legend
F3 = 'f(x)=S1+S2+S3+S4'
F2 = 'f(x)=S1+S2+S3'
F1 = 'f(x)=S1+S2'

#Display Legends
plt.legend(['f(x)','F1','F2','F3'], loc='best')

# Display the triangular wave drawn
plt.show()


# In[67]:


#Showing Data for the Sinusoidal Compositions of the Triangular Wave
FS = pd.read_excel (r'C:\Users\hp\Documents\Downloads\Fourier Series_Waveforms.xlsx', sheet_name='Triangular')
TWC = pd.DataFrame(FS, columns= ['f(x)','S1(n=1)','S2(n=3)','S3(n=5)','S4(n=7)'])

TWC.head()
TWC


# In[68]:


#Plotting Triangular Wave Compositions
plt.plot(TWC)
  

# Give a title for the triangular wave plot
plt.title('Triangular Wave Compositions')

# Give x axis label for the triangular wave plot
plt.xlabel('Time Scaled at 1:20ms')


# Give y axis label for the triangular wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both', linestyle='-.')

 
# Provide x axis and line color
plt.axhline(y=0, color='k')

 
# Set the max and min values for y axis
plt.ylim(-1.5, 1.5)

#Display Legends
plt.legend(['f(x)','S1(n=1)','S2(n=3)','S3(n=5)','S4(n=7)'], loc='best')

# Display the triangular wave drawn
plt.show()


# In[ ]:




