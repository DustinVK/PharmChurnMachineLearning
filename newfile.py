
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