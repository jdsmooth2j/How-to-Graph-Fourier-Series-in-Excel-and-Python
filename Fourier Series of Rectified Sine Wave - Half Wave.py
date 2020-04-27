#!/usr/bin/env python
# coding: utf-8

# In[196]:


import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
plt.get_backend()
'Qt4Agg'
plt.clf()
plt.cla()
plt.close()


# In[198]:


#Fourier Series of Rectified Sine Wave - Half Wave Formula
print('f(x)= 1/π + 0.5*sin(x)- (2/π)*Σ(cos(2nx)/(4n^2 - 1)) from n=1 to ∞')
print('Note: Period, T = 2L')
print('Data from Excel has a period T=2π')

#Open image file for the formula in detail
from PIL import Image
img  = Image.open("Desktop/Half-Wave Rectified Sine Wave.jpg","r")
img.show()


# In[199]:


#Showing Data for the Approximations of the Rectified Sine Wave - Full Wave
FS = pd.read_excel (r'C:\Users\hp\Documents\Downloads\Fourier Series_Waveforms.xlsx', sheet_name='Rect. Sine-HW')
RSHA = pd.DataFrame(FS, columns= ['f(x)','f(x)=S1+S2','f(x)=S1+S2+S3','f(x)=S1+...+S5','f(x)=S1+...+S7'])

RSHA.head()
RSHA


# In[204]:


#Plotting Rectified Sine Wave - Half Wave Approximations from Sums of Sinusoidal Compositions
plt.plot(RSHA)
  

# Give a title for the Rectified Sine Wave - Half Wave plot
plt.title('Rectified Sine Wave - Half Wave Approximations')


# Give x axis label for the Rectified Sine Wave - Half Wave plot
plt.xlabel('Time Scaled at 1:20ms')


# Give y axis label for the Rectified Sine Wave - Half Wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both', linestyle='-.')

 
# Provide x axis and line color
plt.axhline(y=0, color='k')

 
# Set the max and min values for y axis
plt.ylim(-0.2, 1.2)

#Legend
F4 = 'f(x)=f(x)=S1+...+S7'
F3 = 'f(x)=f(x)=S1+...+S5'
F2 = 'f(x)=S1+S2+S3'
F1= 'f(x)=S1+S2'

#Display Legends
plt.legend(['f(x)','F1','F2','F3','F4'], loc='best')

# Display the Rectified Sine Wave - Half Wave drawn
plt.show()


# In[206]:


#Showing Data for the Sinusoidal Compositions of the Rectified Sine Wave - Half Wave
FS = pd.read_excel (r'C:\Users\hp\Documents\Downloads\Fourier Series_Waveforms.xlsx', sheet_name='Rect. Sine-HW')
RSHC = pd.DataFrame(FS, columns= ['f(x)','S1(n=1)','S2(n=2)','S3(n=3)','S4(n=4)','S5(n=5)','S6(n=6)','S7(n=7)'])

RSHC.head()
RSHC


# In[212]:


#Plotting Rectified Sine Wave - Half Wave Compositions
plt.plot(RSHC)
  

# Give a title for the Rectified Sine Wave - Half Wave plot
plt.title('Rectified Sine Wave - Half Wave Compositions')

# Give x axis label for the Rectified Sine Wave - Half Wave plot
plt.xlabel('Time Scaled at 1:20ms')


# Give y axis label for the Rectified Sine Wave - Half Wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both', linestyle='-.')

 
# Provide x axis and line color
plt.axhline(y=0, color='k')

 
# Set the max and min values for y axis
plt.ylim(-0.25, 1.25)


#Display Legends
plt.legend(['f(x)','S1(n=1)','S2(n=2)','S3(n=3)','S4(n=4)','S5(n=5)','S6(n=6)','S7(n=7)'], loc='best')

# Display the Rectified Sine Wave - Half Wave drawn
plt.show()


# In[ ]:




