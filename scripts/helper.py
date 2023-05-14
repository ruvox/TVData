
import os
from .defs import *
import csv

def ls_tables():
    return os.listdir(ps_tables_path)


def csv2dic(full_name):
    dict1 = {}
    with open(full_name, "r") as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        for row in reader:
            dict1[row[0]] = {key: value for key,
                             value in zip(headers[1:], row[1:])}

    return dict1

def read_csv(table_name, csv_file):
    return csv2dic(os.path.join( ps_tables_path, table_name, csv_file)) 

def read_all_table(TV):   
    dict1 = {}
    for table in os.listdir(os.path.join(ps_tables_path, TV)):
        dict1[table] = csv2dic(os.path.join(ps_tables_path, TV, table))
    
    return dict1


def read_meta_table(TV):   
    return csv2dic(os.path.join( ps_tables_path, TV, "Meta.csv")) 
    
def read_table(TV=""):   
    if(TV):
        return csv2dic(os.path.join( ps_tables_path, TV, "Table.csv")) 
    
    dict1 = {}
    for table in os.listdir(ps_tables_path):
        dict1[table] = csv2dic(os.path.join(ps_tables_path, table, "Table.csv"))    
    
    return dict1

def read_tvl_alg(full_path, path):
    return csv2dic(os.path.join(
            full_path, path, "data", path+"-Adv.csv"))