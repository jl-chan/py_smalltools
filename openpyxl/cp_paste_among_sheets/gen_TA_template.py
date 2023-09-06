import pandas as pd
from openpyxl import load_workbook
from utils_openpyxl import *

# Load the Excel file
file_path = 'ABC.xlsx'
df = pd.read_excel(file_path, sheet_name='Log Source List')
print(df)

# Python program to read an excel file
# import openpyxl module
import openpyxl
wb_obj = openpyxl.load_workbook(file_path)
ws = wb_obj['Log Source List']

# Pre-check how many data-model are in used, in order to build a dictionary counters and also to create the sheet if it's not created yet.
in_use_dms = []
for index, row in df.iterrows():
    in_use_dm = row['data model'].split()
    for x in in_use_dm:
        in_use_dms.append(x)
# Dedup the list
deduplicated_in_use_dms = list(dict.fromkeys(in_use_dms))
counter_dict = {item: 0 for item in deduplicated_in_use_dms}
#print(counter_dict['Authentication'])

# Create the sheet if it's not created yet
for x in deduplicated_in_use_dms:
    sheetnm = f'DM-{x}'
    if sheetnm not in wb_obj.sheetnames:
        # Create the sheet if it doesn't exist
        new_ws = wb_obj.create_sheet(title=sheetnm)

row_offset = 40
for index, row in df.iterrows():
    # print(len(row)) # 4
    data_model = row['data model'].split()
    #print(f"Current index is {index}\n")
    #print(f"Current row is {row}\n")
    #print(data_model)
    # For every available data_model, create the template in the respective sheet
    for dm in data_model:
        to_write_sheet_name = wb_obj[f'DM-{dm}']
        ## Copy header
        copy_range(f"A1:{chr(65+len(row)-1)}1", ws, to_write_sheet_name, counter_dict[dm])
        ### Copy cell values to new row
        row_range = f"A{index+2}:{chr(65+len(row)-1)}{index+2}"
        copy_range(row_range, ws, to_write_sheet_name, counter_dict[dm]-index)

        # Add counter per dm
        counter_dict[dm] += row_offset

wb_obj.save("test.xlsx")

###### Some common openpyxl function(s) #######
# Get all sheetnames
# print (wb_obj.sheetnames)

# Get workbook active sheet object
# sheet_obj = wb_obj.active
