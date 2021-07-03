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

data = pd.read_csv('processed_data.csv')
target = pd.read_csv('out_of_time_test_oct.csv')
iris = load_iris()


##  Preprocessing 
target = target.sort_values(by=['customer_ref_id'])
data=data.drop(["customer_ref_id"],axis=1)
target=target.drop(["customer_ref_id"], axis=1)

# Feature Scaling
#scaler = preprocessing.MinMaxScaler()
#names = data.columns
#scaled_data = scaler.fit_transform(data)
#scaled_data = pd.DataFrame(scaled_data, columns=names)
#print(scaled_df.head())


model = tree.DecisionTreeClassifier()
model = model.fit(data,ravel(target))

prediction = model.predict(data)

def measure_error(pred):
    print("Confusion Matrix: \n", metrics.confusion_matrix(target,pred))
    print("Accuracy: \n", metrics.accuracy_score(target, pred))
    print("Recall: \n", metrics.recall_score(target,pred))
    print("Precision: \n", metrics.precision_score(target,pred))
    print("F1 Score: ", metrics.f1_score(target,pred))

print("Decision Tree Results:")
measure_error(prediction)
# Cross Validation
#result = cross_validate(model,data,ravel(target))
#print(result['test_score'])

# export model 
dump(model, 'DTC-model.joblib') 

# test model
print(model.predict([[0.0,0.0,21.0,0.0,0.0,7.0,0.0,3.0,0.0,0.0,18.0,5262.66,6.0,0.0,0.0,15.0,1.0,4228.9485,1,0.0,0.0,0.0]]))

model = linear_model.LogisticRegression(max_iter=900)
model = model.fit(data,ravel(target))

prediction = model.predict(data)
print("Logistic Regression Results:")
measure_error(prediction)

# export model 
dump(model, 'LR-model.joblib') 

# test model
print(model.predict([[0.0,0.0,21.0,0.0,0.0,7.0,0.0,3.0,0.0,0.0,18.0,5262.66,6.0,0.0,0.0,15.0,1.0,4228.9485,1,0.0,0.0,0.0]]))


model = ensemble.RandomForestClassifier()
model = model.fit(data,ravel(target))

prediction = model.predict(data)
print("Random Forest Classifier Results:")
measure_error(prediction)

# export model 
dump(model, 'RF-model.joblib') 

# test model
print(model.predict([[0.0,0.0,21.0,0.0,0.0,7.0,0.0,3.0,0.0,0.0,18.0,5262.66,6.0,0.0,0.0,15.0,1.0,4228.9485,1,0.0,0.0,0.0]]))


