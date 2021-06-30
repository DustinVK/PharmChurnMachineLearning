import tkinter as tk
from joblib import load

lr = load('lr-model.joblib')

attributes = ["quantity_ethical","cash","quantity_acute","cheque","upi","quantity_ayurvedic","returned_quantity_bill","paytm","quantity_general","quantity_chronic","quantity_otc","total_spend_bill","return_value_bill","quantity_surgical","total_quantity_bill","phonepe","card","num_drugs_bill","quantity_generic","mrp_bill","transaction_count","quantity_h1"]
window = tk.Tk()
labels = []
entries = []


for attribute in attributes:
    label = tk.Label(text=attribute)
    entry = tk.Entry()
    labels.append(label)
    entries.append(entry)

for i in range(5):
    for j in range(7):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        if ((i+j) < len(attributes)):
            label = tk.Label(master=frame, text=attributes[i+j])
            entry = tk.Entry(master=frame)
            entry.insert(0,0)
            label.pack()
            entry.pack()
        if (i==4 and j==6):
            button = tk.Button(
                master=frame,
                text="Click me!",
                width=25,
                height=5,
                bg="blue",
                fg="black",
            )
            button.pack()
        







def handle_keypress(event):
    """Print the character associated to the key pressed"""
    name = entry.get()
    print(name)
    print(event.char)

def handle_button(event):
    name = entry.get()
    print(name)

button.bind("<Button-1>", handle_button)
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()
#print(lr.predict([[0.0,0.0,2.0,0.0,0.0,1.0,2.0,2.0,0.0,0.0,0.0,17.2,0.0,0.0,0.0,0.0,0.0,15.48,1,0.0,1.0,0.0]]))

