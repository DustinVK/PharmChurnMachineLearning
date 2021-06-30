from numpy.core.fromnumeric import ravel
import sklearn as sk
from sklearn import ensemble
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
import pandas as pd
import tkinter as tk
import numpy as np 
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn import preprocessing
from sklearn import metrics

from sklearn.datasets import load_iris

from joblib import dump, load

data = pd.read_csv('processed_data2.csv')
target = pd.read_csv('out_of_time_test_oct.csv')
iris = load_iris()


##  Preprocessing 
target = target.sort_values(by=['customer_ref_id'])
#print(target.tail())
#print(data.tail())
data=data.drop(["customer_ref_id"],axis=1)
target=target.drop(["customer_ref_id"], axis=1)

scaler = preprocessing.MinMaxScaler()
names = data.columns
d = scaler.fit_transform(data)
#data = pd.DataFrame(d, columns=names)
#print(scaled_df.head())
#dtc = tree.DecisionTreeClassifier()
#dtc = dtc.fit(data, target)

#rfc = ensemble.RandomForestClassifier()
#rfc = rfc.fit(data, ravel(target))

lr = linear_model.LogisticRegression(max_iter=1000)
lr = lr.fit(data,ravel(target))

#result = cross_validate(dtc,data,target)
#print(result['test_score'])

#result = cross_validate(rfc,data,ravel(target))
#print(result['test_score'])
prediction = lr.predict(data)

print("Confusion Matrix: \n", metrics.confusion_matrix(target,prediction))
print("Accuracy: \n", metrics.accuracy_score(target, prediction))
print("Recall: \n", metrics.recall_score(target,prediction))
print("Precision: \n", metrics.precision_score(target,prediction))
print("F1 Score: ", metrics.f1_score(target,prediction))
result = cross_validate(lr,data,ravel(target))
print(result['test_score'])

dump(lr, 'lr-model.joblib') 

#print(clf.predict([[0.0,0.0,21.0,0.0,0.0,7.0,0.0,3.0,0.0,0.0,18.0,5262.66,6.0,0.0,0.0,15.0,1.0,4228.9485,1,0.0,0.0,0.0
#]]))



