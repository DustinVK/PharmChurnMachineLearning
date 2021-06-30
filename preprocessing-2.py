import sys
import csv
import json

REAL_DATA = 'purchase_data_bill_level_sept.csv'
TEST_DATA = 'test.csv'
TARGET = 'out_of_time_test_oct.csv'

data_list = []
target_map = dict()

with open(TARGET, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    line_count = 0
    fieldnames = []
    
    for row in csv_reader:        
        col_count = 0
        id = 0
        value = 0
        for column in row:
            if (line_count == 0):
                fieldnames.append(column)
            if (col_count == 0):
                id = int(column)
            if (col_count == 1):
                value = int(column)
            col_count += 1
        if (line_count > 0):
            target_map[id] = value
        line_count+=1

with open(REAL_DATA, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    line_count = 0
    fieldnames = []

    for row in csv_reader:        
        col_count = 0
        id = float(row[2])
        record = dict()
        for column in row:
            if (line_count == 0):
                fieldnames.append(column)
            if (line_count > 0):
                
            if (col_count == 0):
                id = int(column)
            if (col_count == 1):
                value = int(column)
            col_count += 1
        if (line_count > 0):
            target_map[id] = value
        line_count+=1


