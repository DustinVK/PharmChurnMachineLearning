# Pharmacy Customer Churn Prediction App
### A machine learning application built with python 3. 

## About
The goal of this app is to predict whether a given customer will make a purchase in the next month. It uses a machine learning model created and trained using the Scikit-learn library.

## Data
The dataset was sourced from Kaggle. It spans 6 months and 1,184,025 records with 21 columns of customer transactional data. 

The training dataset (purchase_data_bill_level_sept.csv) is too big to be hosted on GitHub, but it can be found here:
https://www.kaggle.com/mishra5001/customer-churn-prediction-pharmaceutical-data

## Running the App
This app uses a GUI built with the Tkinter python library. To ensure you have this installed, open a terminal and enter:
```
python -m tkinter
```
If a window pops up showing which version of Tkinter is installed, then you are all set. If not, then you will need to [install it.](https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
)

Then, either clone the repo or just download both application.py and lr-model.joblib to the same directory. Now you can run the app by entering the following from the directory it is in:
```
python3 application.py
```
Once the app is up and running, you can enter in different values and press the prediction button to see the model's prediction. You can also use the randomize button to make entering values quicker. The randomize function will randomize the data based on the actual minimum and maximum values for each field from the training dataset.
