import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt
# handle missing values 
data = {
    "colors" : ['red','green','blue','orange','green','blue',np.nan]
}
df = pd.DataFrame(data)
print(df)
# handle missing values
df.dropna(inplace= True)
print(df)