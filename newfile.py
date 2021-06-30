
import sys
import csv
import json

REAL_DATA = 'purchase_data_bill_level_sept.csv'
TEST_DATA = 'test.csv'

data_map = dict()
data_list = []

def new_row(customer_ref_id):
    data_row = {
        "customer_ref_id":customer_ref_id,
        "cash":0,
        "card":0,
        "cheque":0,
        "paytm":0,
        "phonepe":0,
        "upi":0,
        "transaction_count":1,
        "num_drugs_bill":0,
        "total_quantity_bill":0,
        "mrp_bill":0,
        "total_spend_bill":0,
        "return_value_bill":0,
        "returned_quantity_bill":0,
        "quantity_ethical":0,
        "quantity_generic":0,
        "quantity_surgical":0,
        "quantity_ayurvedic":0,
        "quantity_general":0,
        "quantity_otc":0,
        "quantity_chronic":0,
        "quantity_acute":0,
        "quantity_h1":0
    }
    return data_row

def add_payment_count(row, payment_type):
    if (not payment_type):
        return
    else:
        row[payment_type] += 1

def process_row(row):
    count = row["transaction_count"]
    for key, value in row.items():
        if (key != "transaction_count" and key != "customer_ref_id"):
            row[key] = value/count
    data_list.append(row)

with open(TEST_DATA,newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    line_count = 0
    fieldnames = []
    
    for row in csv_reader:
        data_row = dict()
        id = row[2]
        
        if(line_count > 0):
            if(row[2] in data_map):
                data_row = data_map[id]
                data_row["transaction_count"] +=1
            else:
                data_row = new_row(id)
        
        col_count = 0
        for column in row:
            if (line_count == 0):
                fieldnames.append(column)
            elif (col_count > 3):
                if(fieldnames[col_count] == "payment_method"):
                    add_payment_count(data_row, column)
                elif (col_count > 5):
                    data_row[fieldnames[col_count]] += float(column)
            col_count += 1
        if (line_count > 0):
            data_map[id] = data_row
        
        line_count+=1

for key, value in data_map.items():
    process_row(value)

def func(e):
    return e['customer_ref_id']

data_list.sort(key=func)

print(data_list)

label0 = tk.Label(text="Avg Quantity Ethical (0-500)")
entry0 = tk.Entry()
label1 = tk.Label(text="Cash (0-1)")
entry1 = tk.Entry()
label2 = tk.Label(text="Avg Quantity Acute (0-1510)")
entry2 = tk.Entry()
label3 = tk.Label(text="Cheque (0-1)")
entry3 = tk.Entry()
label4 = tk.Label(text="UPI (0-1)")
entry4 = tk.Entry()
label5 = tk.Label(text="Avg Quantity Ayurvedic (0-23)")
entry5 = tk.Entry()
label6 = tk.Label(text="Avg Returned Quantity Bill, (0-1500)")
entry6 = tk.Entry()
label7 = tk.Label(text="paytm (0-1)")
entry7 = tk.Entry()
label8 = tk.Label(text="Avg Quantity General (0-366)")
entry8 = tk.Entry()
label9 = tk.Label(text="Avg Quantity Chronic (0-300)")
entry9 = tk.Entry()
label10 = tk.Label(text="AVG Quantity OTC (0-40")
entry10 = tk.Entry()
label11 = tk.Label(text="Avg Total Spend Bill (6-64000)")
entry11 = tk.Entry()
label12 = tk.Label(text="Avg Return Value Bill (0-30000)")
entry12 = tk.Entry()
label13 = tk.Label(text="Avg Quantity Surgical (0-412)")
entry13 = tk.Entry()
label14 = tk.Label(text="Avg Total Quantity Bill (0-1514)")
entry14 = tk.Entry()
label15 = tk.Label(text="Phonepe (0-1)")
entry15 = tk.Entry()
label16 = tk.Label(text="Card (0-1)")
entry16 = tk.Entry()
label17 = tk.Label(text="Avg Num Drugs Bill (0-48)")
entry17 = tk.Entry()
label18 = tk.Label(text="Avg Quantity Generic (0-1000)")
entry18 = tk.Entry()
label19 = tk.Label(text="Avg MRP Bill (.95 - 199620)")
entry19 = tk.Entry()
label20 = tk.Label(text="Transaction Count (1-47850)")
entry20 = tk.Entry()
label21 = tk.Label(text="Avg Quantity H1 (1-56)")
entry21 = tk.Entry()

label0.pack()
entry0.pack()
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label4.pack()
entry4.pack()
label5.pack()
entry5.pack()
label6.pack()
entry6.pack()
label7.pack()
entry7.pack()
label8.pack()
entry8.pack()
label9.pack()
entry9.pack()
label10.pack()
entry10.pack()
label11.pack()
entry11.pack()
label12.pack()
entry12.pack()
label13.pack()
entry13.pack()
label14.pack()
entry14.pack()
label15.pack()
entry15.pack()
label16.pack()
entry16.pack()
label17.pack()
entry17.pack()
label18.pack()
entry18.pack()
label19.pack()
entry19.pack()
label20.pack()
entry20.pack()
label21.pack()
entry21.pack()