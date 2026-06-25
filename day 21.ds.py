import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
# subplot 1D

#graph one data
year = [2010,2015,2020,2025]
dairy = [100,520,630,400]

#graph two data
year = [1990,2000,2005,2010]
farming = [300,200,250,100]

#this is first graph
fig,aux = plt.subplots(1,2)
aux[0].plot(year,farming)  # first col for line chart
aux[0].set_xlabel("year")
aux[0].set_ylabel("dairy")
aux[0].set_title("dairy production graph")

# this is second graph
aux[1].plot(year,dairy)  # second col for line chart
aux[1].set_xlabel("year")
aux[1].set_ylabel("farming")
aux[1].set_title("dairy production graph")
# Text(0.5, 1.0, 'dairy production graph')