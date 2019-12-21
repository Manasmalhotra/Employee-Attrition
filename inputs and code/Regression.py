import pandas as pd
import xlrd
import numpy as np
import seaborn as sns
import matplotlib as mat
import matplotlib.pyplot as plt
import pickle
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#reading data.
f=pd.read_csv('combined data.csv')

#getting dummy variables to replace categorical variables.

sal=pd.get_dummies(f['salary'],drop_first=True)
dep=pd.get_dummies(f['dept'])
f=pd.concat([f,sal,dep],axis=1)
f.drop(['dept','salary','Emp ID'],axis=1,inplace=True)
f.to_csv('finalised dataset.csv',sep=',')

#Proceeding with Regression after preprocessing of data.

x=f.drop(['left','Unnamed: 0'],axis=1)
y=f["left"]

#Dividing data into training and testing dataset and fitting it on training set.

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)
log=LogisticRegression()
log.fit(X_train,y_train)
X_test.to_csv('Inputs.csv',sep=',')
predictions=pd.DataFrame(log.predict(X_test))
predictions.to_csv('Results.csv',sep=',')
#saving our model for future use.
filename = 'finalized_model.sav'
pickle.dump(log, open(filename, 'wb'))

#Analysing accuracy of the model.
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))
print("The accuracy is",accuracy_score(y_test,predictions))

#Another method found during research,but after submission of proof of concept-The Gradient Booster Classifier.
#I have thus used only Logistic Regression for all the predictions.

from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier()
gb.fit(X_train, y_train)

y_pred = gb.predict(X_test)
print("Accuracy of gradient booster:",accuracy_score(y_test, y_pred))

