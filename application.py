import tkinter as tk
from tkinter import *
from joblib import load
import random

lr = load('lr-model.joblib')

attributes = ["quantity_ethical","cash","quantity_acute","cheque","upi","quantity_ayurvedic","returned_quantity_bill","paytm","quantity_general","quantity_chronic","quantity_otc","total_spend_bill","return_value_bill","quantity_surgical","total_quantity_bill","phonepe","card","num_drugs_bill","quantity_generic","mrp_bill","transaction_count","quantity_h1"]
window = tk.Tk()
window.title('Customer Churn Prediction')
prediction_text = "Press the 'Make Prediction' Button... "
labels = []
entries = []


#for attribute in attributes:
    #label = tk.Label(text=attribute)
    #entry = tk.Entry()
    #labels.append(label)
    #entries.append(entry)

attribute_index = 0
for i in range(6):
    for j in range(5):
        frame = LabelFrame(window,padx=5,pady=5,relief=FLAT)
        frame.grid(row=i, column=j, sticky='EW')
        if (attribute_index < len(attributes)):
            label = tk.Label(master=frame, text=attributes[attribute_index])
            attribute_index += 1
            entry = tk.Entry(master=frame)
            entries.append(entry)
            entry.insert(0,0)
            label.pack()
            entry.pack()
        elif (attribute_index == len(attributes)):
            frame.grid(row=i, column=j, columnspan=3)
            prediction_label = tk.Label(master=frame, text="Press the 'Make Prediction' Button...", )
            prediction_label.pack()
            attribute_index += 1
        if (i == 5 and j == 0):
            prediction_button = tk.Button(
                master=frame,
                text="Make Prediction",
                activeforeground="red",
            )
            prediction_button.pack()
        if (i == 5 and j == 1):
            random_button = tk.Button(
                master=frame,
                text="Randomize...",
                activeforeground="yellow",
            )
            random_button.pack()





def handle_keypress(event):
    """Print the character associated to the key pressed"""
    name = entry.get()
    print(name)

def make_prediction(event):
    row = []
    for thing in entries:
        row.append(float(thing.get()))
    prediction = lr.predict([[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21]]])
    prediction_text = ""
    if (prediction == 0):
        prediction_text = "Customer will not make a purchase within the next month."
    else:
        prediction_text = "Customer will make a purcahse within the next month."
    prediction_label.config(text=prediction_text)
    print(lr.predict([[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21]]]))


def randomize(event):
    vals = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    vals[0] = random.uniform(0,500)
    vals[1] = random.uniform(0,1)
    vals[2] = random.uniform(0,1550)
    vals[3] = random.uniform(0,1)
    vals[4] = random.uniform(0,1)
    vals[5] = random.uniform(0,23)
    vals[6] = random.uniform(0,1514)
    vals[7] = random.uniform(0,1)
    vals[8] = random.uniform(0,366)
    vals[9] = random.uniform(0,300)
    vals[10] = random.uniform(0,40)
    vals[11] = random.uniform(0.5,15621)
    vals[12] = random.uniform(0,2573)
    vals[13] = random.uniform(0,412)
    vals[14] = random.uniform(0,1514)
    vals[15] = random.uniform(0,1)
    vals[16] = random.uniform(0,1)
    vals[17] = random.uniform(0,48)
    vals[18] = random.uniform(0,1000)
    vals[19] = random.uniform(1,24118)
    vals[20] = random.randrange(1,10)
    vals[21] = random.uniform(0,56)

    for i in range(len(entries)):
        print(vals[i])
        entries[i].delete(0,tk.END)
        entries[i].insert(0, vals[i])
        
    
  
   

prediction_button.bind("<Button-1>", make_prediction)
random_button.bind("<Button-1>", randomize)
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()
row=[]
#print(lr.predict([[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21]]]))

