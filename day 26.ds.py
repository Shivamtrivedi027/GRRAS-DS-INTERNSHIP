# handle missing values
import pandas as pd
import numpy as np
data = {
    "colors":['red','green','blue','orange','green','blue',np.nan]
}
df = pd.DataFrame(data)
# print(df)

# handle null values
df.dropna(inplace=True)
print(df)

# label encoding
from sklearn.preprocessing import LabelEncoder

# method 1
le = LabelEncoder()
df['colors_encoder1'] = le.fit_transform(df['colors'])

# method 2
df['colors_encoder2'] = LabelEncoder().fit_transform(df['colors'])
# print(df)

# method 3
import sklearn
df['colors_encoder3'] = sklearn.preprocessing.LabelEncoder().fit_transform(df['colors'])
print(df)


# one hot encoding
from sklearn.preprocessing import OneHotEncoder
print(df)

# drop cols of label encoding
if 'colors_encoder' in df.keys():
  df.drop(df[['colors_encoder','colors_encoder1','colors_encoder2','colors_encoder3']],axis=1,inplace=True)

print(df)

# one hot encoding (by the help of sklearn)
encoder = OneHotEncoder()
encoded = encoder.fit_transform(df[['colors']])
print(encoded.toarray())

# one hot encoding (by the help of pandas)
df_encoder = pd.get_dummies(df,columns=['colors'])
print(df_encoder)
     


# combination of handle missing value | label encoding | onehot encoding
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder , OneHotEncoder

data = {
    "age":[10,20,np.nan,26,30],
    "gender":['male','female','others','male',np.nan],
    "name":['dheeraj','kavi','sapu','yash','hello']
}

df = pd.DataFrame(data)

# handle missing values
df['age'] = df['age'].fillna(df['age'].mean())
df.dropna(subset=['gender'],inplace=True)
print(df)

# label encoding
le = LabelEncoder()
df['gender1'] = le.fit_transform(df['gender'])
print(df)

# one hot encoding
oe = OneHotEncoder()
oe_e = oe.fit_transform(df[['gender']]).toarray()
print(oe_e)
     

# feature scaling
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data = {
    "experience":[300,600,900,1500],
    "salary":[1000,1500,2000,3000]
}
# data frame
df = pd.DataFrame(data)
print(df)

# standard scaler
scaler = StandardScaler()
df['experience'] = scaler.fit_transform(df[['experience']]) # 2d
print(df)

# split data exp-> x | sal -> y
X = df['experience'] # capital X
y = df['salary']

print(X)
print(y)

# graph plot
     

# data split training testing
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/extended_salary_data.csv"

df = pd.read_csv(data)
# print(df)

# split data
X = df[['experience']] # capital X -> 2d
y = df['salary']

# train test split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("x train: ",x_train )
print("x test: ",x_test)
print("y train: ", y_train)
print("y test: ", y_test)
     


# simple linear reg | prediction
from sklearn.linear_model import LinearRegression

# model fit
model = LinearRegression()
model.fit(x_train,y_train) # 2d

# input from user
user = int(input("Enter your Experience: "))
# model prediction

new_data = {
    "experience":[user]
}

df1 = pd.DataFrame(new_data)
print(df1)
pred_data = model.predict(df1)
print(pred_data[0])
     
