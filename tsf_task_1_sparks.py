# -*- coding: utf-8 -*-
"""TSF-TASK 1 SPARKS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1608x9in7Isrv5o6eGhnSBR3bEGbNM48d

# THE SPARKS FOUNDATION

## Data Science and Business Analytics Internship

### Author : Amit Kumar

### TASK 1: Prediction Using Supervised Machine Learning

### Problem Statement: Predict the percentage of a student based on the number of hours studied

##  Libraries
"""

#Importing  required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import scipy.stats as stats
import statsmodels.formula.api as smf

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings('ignore')

"""## Loading Dataset"""

# Reading Data 
df = pd.read_csv('http://bit.ly/w-data')
df.head()

"""## Basic discription of data"""

#rows and columns
print(df.shape)

#Information of data
df.describe()

# null values in dataset
df.isnull().sum()

"""## EDA of Data"""

#Plotting  dataset
sns.distplot(df["Scores"])
plt.show()

sns.distplot(df["Scores"], kde=False, rug=True)
plt.show()

# Plotting the distribution of score
plt.figure(figsize=(12,6))
plt.title('Scores vs Hours', size=20)
plt.xlabel('Hours Study', size=15)
plt.ylabel('Percentage Score', size=15)
plt.scatter(df.Hours,df.Scores,color='blue')
plt.show()

#correlationn between two variables 
df.corr()

"""## Featur Engineering """

x=df.iloc[:, :-1].values
y=df.iloc[:,1].values

x

y

"""## Splitting Dataset Into Train and Test"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

"""## Model Preparation """

regressor=LinearRegression()
regressor.fit(x_train.reshape(-1,1),y_train)
print("Training of then model is complete")

"""## Plotting Linear Regression Model"""

#Plotting the regression line
line=regressor.coef_*x+regressor.intercept_

#Plotting the scatter plot with the regression line
plt.scatter(x,y,color='green',marker='o')
plt.plot(x,line,color='red');
plt.title('Graphical relationship between the number of study hours and scores obtained')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Scored(%)')
plt.show()

print('intercept={}, slope coefficient={}'.format(regressor.intercept_,regressor.coef_))

"""## Predicting  Using Linear Regression Model"""

print(x_test)
y_pred=regressor.predict(x_test)

"""## Comparing Actual and Predicted Results"""

data=pd.DataFrame({'Actual': y_test,'Predicted':y_pred})
data

from sklearn import metrics
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,y_pred))
print('Mean Squared Error:',metrics.mean_squared_error(y_test,y_pred))
print('Root Mean Squared Error',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))
print('R2:',metrics.r2_score(y_test,y_pred))

"""## Testing of Model"""

hours=9.25
test=np.array([hours])
test=test.reshape(-1,1)
own_pred=regressor.predict(test)
print("No. of hours={}".format(hours))
print("Predicted Score={}".format(own_pred[0]))

"""## predicted score of a person studying for 9.25 hours is 92.92"""