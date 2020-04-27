#!/usr/bin/env python
# coding: utf-8

# In[156]:


import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
plt.get_backend()
'Qt4Agg'
plt.clf()
plt.cla()
plt.close()


# In[172]:


#Sawtooth Wave Formula
print('f(x)= Σ(2*((-1)^(n+1))/(nπ))*sin(nπx)) from n=1 to ∞')
print('Note: Period, T = 2L')
print('Data from Excel has a period T=2')

#Open image file for the formula in detail
from PIL import Image
img  = Image.open("Desktop/Sawtooth Wave.jpg","r")
img.show()


# In[173]:


#Showing Data for the Approximations of the Sawtooth Wave
FS = pd.read_excel (r'C:\Users\hp\Documents\Downloads\Fourier Series_Waveforms.xlsx', sheet_name='Sawtooth')
STWA = pd.DataFrame(FS, columns= ['f(x)','f(x)=S1+S2+S3','f(x)=S1+...+S5','f(x)=S1+...+S7'])

STWA.head()
STWA


# In[181]:


#Plotting Sawtooth Wave Approximations from Sums of Sinusoidal Compositions
plt.plot(STWA)
  

# Give a title for the sawtooth wave plot
plt.title('Sawtooth Wave Approximations')


# Give x axis label for the sawtooth wave plot
plt.xlabel('Time Scaled at 1:20ms')


# Give y axis label for the sawtooth wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both', linestyle='-.')

 
# Provide x axis and line color
plt.axhline(y=0, color='k')

 
# Set the max and min values for y axis
plt.ylim(-1.5, 1.5)

#Legend
F3 = 'f(x)=f(x)=S1+...+S7'
F2 = 'f(x)=f(x)=S1+...+S5'
F1 = 'f(x)=S1+S2+S3'

#Display Legends
plt.legend(['f(x)','F1','F2','F3'], loc='best')

# Display the sawtooth wave drawn
plt.show()


# In[182]:


#Showing Data for the Sinusoidal Compositions of the Sawtooth Wave
FS = pd.read_excel (r'C:\Users\hp\Documents\Downloads\Fourier Series_Waveforms.xlsx', sheet_name='Sawtooth')
STWC = pd.DataFrame(FS, columns= ['f(x)','S1(n=1)','S2(n=2)','S3(n=3)','S4(n=4)','S5(n=5)','S6(n=6)','S7(n=7)'])

STWC.head()
STWC


# In[183]:


#Plotting Sawtooth Wave Compositions
plt.plot(STWC)
  

# Give a title for the sawtooth wave plot
plt.title('Sawtooth Wave Compositions')

# Give x axis label for the sawtooth wave plot
plt.xlabel('Time Scaled at 1:20ms')


# Give y axis label for the sawtooth wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both', linestyle='-.')

 
# Provide x axis and line color
plt.axhline(y=0, color='k')

 
# Set the max and min values for y axis
plt.ylim(-1.25, 1.25)



#Display Legends
plt.legend(['f(x)','S1(n=1)','S2(n=2)','S3(n=3)','S4(n=4)','S5(n=5)','S6(n=6)','S7(n=7)'], loc='best')

# Display the sawtooth wave drawn
plt.show()


# In[ ]:




