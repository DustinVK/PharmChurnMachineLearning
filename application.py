import tkinter as tk
from joblib import load

lr = load('lr-model.joblib')

attributes = ["quantity_ethical","cash","quantity_acute","cheque","upi","quantity_ayurvedic","returned_quantity_bill","paytm","quantity_general","quantity_chronic","quantity_otc","total_spend_bill","return_value_bill","quantity_surgical","total_quantity_bill","phonepe","card","num_drugs_bill","quantity_generic","mrp_bill","transaction_count","quantity_h1"]
window = tk.Tk()
labels = []
entries = []


#for attribute in attributes:
    #label = tk.Label(text=attribute)
    #entry = tk.Entry()
    #labels.append(label)
    #entries.append(entry)


attribute_index = 0
for i in range(5):
    for j in range(5):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        if (attribute_index < len(attributes)):
            label = tk.Label(master=frame, text=attributes[attribute_index])
            attribute_index += 1
            entry = tk.Entry(master=frame)
            entries.append(entry)
            entry.insert(0,0)
            label.pack()
            entry.pack()
   

        if (i==4 and j==4):
            button = tk.Button(
                master=frame,
                text="Make Prediction",
                width=25,
                height=5,
                bg="blue",
                fg="black",
            )
            button.pack()
        

prediction_label = tk.Label(master=frame)
prediction_label.pack()





def handle_keypress(event):
    """Print the character associated to the key pressed"""
    name = entry.get()
    print(name)

def handle_button(event):
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

   

button.bind("<Button-1>", handle_button)
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()
row=[]
#print(lr.predict([[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21]]]))

